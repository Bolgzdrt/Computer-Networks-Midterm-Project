# ICMP Ping Tool

Assignment 3

Ping is a popular networking application used to test from a remote location whether a particular host is up and reachable. It is also often used to measure latency between the client host and the target host. It works by sending ICMP “echo request” packets (i.e., ping packets) to the target host and listening for ICMP “echo response” replies (i.e., pong packets). Ping measures the RRT, records packet loss, and calculates a statistical summary of multiple ping-pong exchanges (the minimum, mean, max, and standard deviation of the round-trip times).\n

In this assig, you will write your own Ping application in (Python or any language). Your application will use ICMP. But in order to keep your program simple, you will not exactly follow the official specification in RFC 1739.
