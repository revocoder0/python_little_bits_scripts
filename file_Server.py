import socket

s= socket.socket()
host = "127.0.0.1"
port = 80

s.bind((host, port))
s.listen(1)

print("waiting for any incomming connection form ", port)

conn, addr = s.accept()


print(addr, " has connected to server.")

#File Transfer....
fileName= input("Please enter the filename of the file...: ")
file=open(fileName, 'rb')
file_data=file.read(1024)
conn.send(file_data)
print("Data has been transmitted success...")