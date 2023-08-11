import socket

target = '192.168.1.1'

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except socket.error as e:
        print(f"Error encountered: {e}")
        return False

for port in range(1, 1024):
    result = portscan(port)

    if result:
        print(f'Port: {port} is open')
    else:
        print(f'Port: {port} is closed')