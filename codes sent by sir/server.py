import socket

s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = 12345

s.bind((host,port))

s.listen()
print("SERver is listing to clients ")
while True :
    conn, addr = s.accept()   
    print("Got connection from ",*addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='mytext.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()
