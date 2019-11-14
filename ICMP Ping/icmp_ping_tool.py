from pythonping import ping     # used to send ICMP packet to desired destination
import time                     # used to space out pings
import statistics               # used for mean and std deviation calcs

destination = input("Address to ping: ")
num_packets = input("Number of packets: ")
num_packets = int(num_packets)
i = num_packets

max_rtt = 0
min_rtt = 99999999999
rtts = []
missed_packets = 0

print()

while i != 0:
    # response is an object with data from sending/receiving
    # packets to/from destination IP
    response = ping(destination, count=1)
    # print response from destination, _responses is a list
    print(response._responses[0])
    
    # record if lost packet
    if str(response._responses[0]) == "Request timed out":
        missed_packets += 1
    # check if maximum RTT
    if response.rtt_avg_ms > max_rtt:
        max_rtt = response.rtt_avg_ms
    # check if minimum RTT
    if response.rtt_avg_ms < min_rtt:
        min_rtt = response.rtt_avg_ms
    rtts.append(response.rtt_avg_ms)

    i -= 1
    # wait to send next packet
    time.sleep(1)

# packet loss calculation
packet_loss = (missed_packets/num_packets)

# output ping statistics
print("\nPacket Loss: " + "{:.2%}".format(packet_loss))
print("Min RTT: ", min_rtt)
print("Max RTT: ", max_rtt)
print("Avg RTT: ", statistics.mean(rtts))
print("Std Deviation of RTT: ", statistics.stdev(rtts))