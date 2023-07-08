import socket
import time

HEADERSIZE = 10

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1214))
s.listen(5)

print("Waiting from incomming connection.............")

while True:
    clientsocket, address = s.accept()
    print(f"Connection form {address} has been established!.....")
    msg = "Welcome to  the server!!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg
    clientsocket.send(bytes(msg, "utf-8"))
    
    while True:
        time.sleep(3)
        msg = f"The time is !{time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientsocket.send(bytes(msg,"utf-8"))