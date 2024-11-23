import socket
import rsa
# Define the host and port for the server
host = '127.0.0.1'  # Localhost
port = 12345  # Port to bind the server

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address
server_socket.bind((host, port))

# Enable the server to accept connections (maximum of 5 queued connections)
server_socket.listen(5)

print(f"Server is listening on {host}:{port}...")

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    try:
        while True:
            # Receive the data sent by the client
            data = client_socket.recv(1024)  # Buffer size of 1024 bytes
            if not data:
                break  # Connection was closed or no data received
            message = data.decode('utf-8')

            if message.lower() == 'exit':
                print("Exit command received. Closing connection.")
                break  # Exit the loop if the client sends 'exit'

            print(f"Received message from client: {rsa.decrypt_rsa(rsa.private_key,message)}")

            # Send a response back to the client
            response = "Message received!"
            client_socket.send(response.encode('utf-8'))

    finally:
        # Close the client socket
        client_socket.close()
