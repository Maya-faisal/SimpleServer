# Client UDP
from socket import *
import time

serverPort = 8855
serverName = "192.168.1.255"
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    # Message to send
    message = "Layan Abuershaid"

    # Send message to server
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    print("Sent message..")

    # Wait for 2 seconds
    time.sleep(2)
