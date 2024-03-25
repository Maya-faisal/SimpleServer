from socket import *
import time

serverPort = 8855
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))

print('The server is ready to receive')

clients = {}  # Dictionary to store client addresses and messages

while True:
    # Receive message and client address
    message, clientAddress = serverSocket.recvfrom(1024)

    # Get current time
    T = time.strftime('%H:%M:%S')

    # Decode message from bytes to string
    message_str = message.decode('utf-8')

    # Store client address and message with timestamp
    clients[clientAddress] = (message_str, T)

    # Print server name
    print("Server Name: Alaa Shaheen")

    # Print received messages from clients
    for address, (msg, timestamp) in clients.items():
        print("Received message from", address, ":", msg, "at time:", timestamp)
    print()

    # Check if the client sent a special message to close the connection
    if message_str == 'CLOSE':
        del clients[clientAddress]
        print(f"Client {clientAddress} has closed the connection.")

    last_message = message_str  # Store the last received message
