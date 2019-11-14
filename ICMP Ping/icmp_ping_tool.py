from pythonping import ping
import time
import statistics

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
    response = ping(destination, count=1)
    print(response._responses[0])

    if str(response._responses[0]) == "Request timed out":
        missed_packets += 1
    if response.rtt_avg_ms > max_rtt:
        max_rtt = response.rtt_avg_ms
    if response.rtt_avg_ms < min_rtt:
        min_rtt = response.rtt_avg_ms
    rtts.append(response.rtt_avg_ms)

    i -= 1
    time.sleep(1)

packet_loss = (missed_packets/num_packets)

print("\nPacket Loss: " + "{:.2%}".format(packet_loss))
print("Min RTT: ", min_rtt)
print("Max RTT: ", max_rtt)
print("Avg RTT: ", statistics.mean(rtts))
print("Std Deviation of RTT: ", statistics.stdev(rtts))