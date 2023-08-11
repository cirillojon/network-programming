import socket
import threading
from queue import Queue

target = '192.168.1.1'
queue = Queue()
open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except socket.error as e:
        print(f"Error encountered: {e}")
        return False

''' Inefficient loop that doesn't use multi-threading
for port in range(1, 1024):
    result = portscan(port)

    if result:
        print(f'Port: {port} is open')
    else:
        print(f'Port: {port} is closed')
'''

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print(f'Port: {port} is open')
            open_ports.append(port)

