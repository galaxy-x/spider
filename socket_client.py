import socket
client = socket.socket()
client.connect(('192.168.43.79', 8000))

while True:
    input_data = input()
    client.send(input_data.encode("utf8"))
    client.close()
