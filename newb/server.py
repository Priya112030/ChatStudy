import socket
s = socket.socket()
host = socket.gethostname()
port = 8080
print('Server will start on host:', host)
s.bind((host, port))
print('Waiting for connection...\n')
s.listen(1)
conn, addr = s.accept()
print(addr, 'Has connected to the server\n')
while True:
    message = input(str('>> '))
    message = message.encode()
    conn.send(message)
    print('Sent\n')
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print('Client:', incoming_message)
    print()
