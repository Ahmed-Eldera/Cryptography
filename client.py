import socket
import rsa

# Define the server's host and port
host = '127.0.0.1'  # Server's IP address (localhost for local testing)
port = 12345  # The port the server is listening on

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address
client_socket.connect((host, port))

try:
    while True:
        # Get the message to send to the server
        message = input("Enter message to send to the server (type 'exit' to quit): ")
        message= rsa.encrypt_rsa(rsa.public_key,message)
        # Send the message to the server
        client_socket.send(message.encode('utf-8'))
        print(f"Sent message to server: {message}")

        if message.lower() == 'exit':
            print("Exiting...")
            break  # Exit the loop if the user types 'exit'

        # Receive the response from the server
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode('utf-8')}")

finally:
    # Close the socket
    client_socket.close()
