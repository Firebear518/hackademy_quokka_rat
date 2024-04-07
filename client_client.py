import socket

host = '172.17.0.3'
port = 8282

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

while True:
    message = s.recv(1024).decode()
    print(f"message : {message}")

    data = input("Input your message: ")

    s.send(data.encode())