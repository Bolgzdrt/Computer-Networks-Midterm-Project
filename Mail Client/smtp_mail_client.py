from socket import *

email_content = "This python program is working!"

email_server = ("smtp.gmail.com", 465)

# TCP socket creation
mailSocket = socket(AF_INET, SOCK_STREAM)
mailSocket.connect(email_server)

returnMsg = mailSocket.recv(1024)
if returnMsg[:3] != "220":
    print("Server did not reply")
else:
    print("Connection request: " + returnMsg)

# HELO command to initialize SMTP conversation
heloContent = "HELO smtp.gmail.com"
mailSocket.send(heloContent.encode())
returnMsg = mailSocket.recv(1024)
if returnMsg[:3] != "250":
    print("Server did not reply")
else:
    print(returnMsg)

