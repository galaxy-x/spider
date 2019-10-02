import socket

server = socket.socket();
server.bind(('0.0.0.0', 8000))

server.listen();

sock, addr = server.accept();

data = ""
while True:
    tmp_data = sock.recv(1024)
    print(tmp_data.decode("utf8"))
    input_data = input()
    sock.send(input_data.encode("utf8"))

server.close()

