import socket
s=socket.socket()
print('server started..')
port=1234
h=socket.gethostname()
s.bind((h,port))
print('socket created..')
s.listen(3)
while True:
    c,addr=s.accept()
    msg=str(input('text something: '))
    c.send(msg.encode('utf-8'))
    s.close()
    
