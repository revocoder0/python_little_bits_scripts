import socket

s= socket.socket()
host = "127.0.0.1"
port = 80

s.connect((host, port))
print("Connected.....")


#File recevie

file=open('receive', 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()

print("File has been recived..")