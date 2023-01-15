import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 4000))
message = input("Введіть будь ласка два числа: ")
sock.send(bytes(message, encoding="UTF-8"))
answer = sock.recv(1024)
sock.close()
print(answer.decode("UTF-8"))
