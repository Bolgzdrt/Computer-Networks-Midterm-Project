import socket
import time
import select
import struct
import os
import sys
import binascii

def createChecksum(str_):
    str_ = bytearray(str_)
    checksum = 0
    str_length = (len(str_) // 2) * 2

    if str_length < len(str_):
        checksum = checksum + str_[-1]
        checksum = checksum & 0xffffffff
    else:
        for i in range(0, str_length, 2):
            current_val = str_[i + 1] * 256 + str_[i]
            checksum = checksum + current_val
            checksum = checksum & 0xffffffff

    checksum = (checksum >> 16) + (checksum & 0xffff)
    checksum = checksum + (checksum >> 16)
    result = ~checksum
    result = result & 0xffff
    result = result >> 8 | (result << 8 & 0xff00)
    return result

def receivePing(my_socket, ID, timeout, dest_addr):
    while 1:
        started_select = time.time()
        what_ready = select.select([my_socket], [], [], timeout)
        select_duration = (time.time() - started_select)
        if what_ready[0] == []:
            return "Request timed out"
        
        time_received = time.time()
        rec_packet, addr = my_socket.recvfrom(1024)

        icmp_header = rec_packet[20:28]
        icmp_type, code, checksum, packet_ID, sequence = struct.unpack("bbHHh", icmp_header)

        if type != 8 and packet_ID == ID:
            bytes_in_double = struct.calcsize("d")
            time_sent = struct.unpack("d", rec_packet[28:28 + bytes_in_double])[0]
            return time_received - time_sent

        timeout = timeout - select_duration

        if timeout <= 0:
            return "Request timed out"

def sendPing(my_socket, dest_addr, ID):
    my_checksum = 0
    header = struct.pack("bbHHh", 8, 0, my_checksum, ID, 1)
    data = struct.pack("d", time.time())
    my_checksum = createChecksum(header + data)

    if sys.platform == 'darwin':
        my_checksum = socket.htons(my_checksum) & 0xffff
    else:
        my_checksum = socket.htons(my_checksum)

    header = struct.pack("bbHHh", 8, 0, my_checksum, ID, 1)
    packet = header + data
    my_socket.sendto(packet, (dest_addr, 1))

def doPing(dest_addr, timeout):
    icmp = socket.getprotobyname("icmp")
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, icmp)

    my_ID = os.getpid() & 0xFFFF
    sendPing(my_socket, dest_addr, my_ID)
    delay = receivePing(my_socket, my_ID, timeout, dest_addr)

    my_socket.close()
    return delay

def ping (host, timeout=1):
    dest = socket.gethostbyname(host)
    print("Pinging " + dest + ":\n")

    while 1:
        delay = doPing(dest, timeout)
        print(delay)
        time.sleep(1)
    return delay

ping("127.0.0.1")