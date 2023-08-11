import threading
import socket

# Prompt the user to choose a nickname for the chat
nickname = input("Choose a nickname: ")

# Initialize the client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the client to the server using the localhost IP and port 55555
client.connect(('127.0.0.1', 55555))

def receive():
    """
    Function to receive messages from the server.
    This runs in a loop to keep listening for new messages.
    """
    while True:
        try:
            # Get message from the server
            message = client.recv(1024).decode('ascii')
            
            # If the message is 'NICK', it's a prompt to send the chosen nickname
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                # Print any other received message to the console
                print(f'Message: {message}')
        except Exception as e:
            # Print any error that occurs and close the client's connection
            print(f'An error occurred: {e}')
            client.close()
            break

def write():
    """
    Function to send messages to the server.
    This captures user input and sends it as a message prefixed with the user's nickname.
    """
    while True:
        # Get user input for a message and send it to the server prefixed with the user's nickname
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

# Start the receive function in a separate thread
receives_thread = threading.Thread(target=receive)
receives_thread.start()

# Start the write function in a separate thread
write_thread = threading.Thread(target=write)
write_thread.start()
