import socket

server = socket.socket();
server.bind(('0.0.0.0', 8000))

server.listen();

sock, addr = server.accept();

data = " "
while True:
    tmp_data = socket.recv(1024)
    if tmp_data:
        data += tmp_data
    else:
        break
print(data)
server.close()

