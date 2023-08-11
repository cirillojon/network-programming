import threading 
import socket

# Set up the server address
host = '127.0.0.1' # Use localhost for local testing
port = 55555

# Initialize the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the server to the specified host and port
server.bind((host, port))
# Server starts listening for incoming client connections
server.listen()

# Lists to store connected client sockets and their corresponding nicknames
clients = []
nicknames = []

def broadcast(message):
    """
    Send the provided message to all connected clients.
    """
    for client in clients:
        client.send(message)

def handle(client):
    """
    Handle communication with a specific client.
    """
    while True:
        try:
            # Receive a message from the client
            message = client.recv(1024)
            # Broadcast the received message to all other clients
            broadcast(message)
        except Exception as e:
            # If any exception occurs, remove the client and close the connection
            print(f'Exception: {e}')
            index = clients.index(client)
            clients.remove(client)
            client.close()
            # Notify other clients that this client (nickname) has left the chat
            nickname = nicknames[index]
            broadcast(f'Nickname: {nickname} was removed'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    """
    Server's main loop to accept incoming clients.
    """
    while True:
        # Wait and accept a new client connection
        client, address = server.accept()
        print(f'Connected with {str(address)}')
        
        # Request the client to provide a nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        # Store the client's socket and nickname
        nicknames.append(nickname)
        clients.append(client)

        # Notify about the new client's nickname and notify the client of a successful connection
        print(f'Nickname of client is: {nickname}')
        broadcast(f'{nickname} has joined'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        # Start a new thread to handle this client's messages
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# Notify that the server has started and is listening, then start the main loop
print(f'Server is listening on port: {port}')
receive()
