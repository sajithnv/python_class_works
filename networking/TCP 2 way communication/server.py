import socket
s=socket.socket()
print('server started..')
port=1234
h=socket.gethostname()
s.bind((h,port))
print('socket created..')
s.listen(3)
c,addr=s.accept()
while True:
    msg=str(input('text something: '))
    c.send(msg.encode('utf-8'))
    m=c.recv(1000)
    m1=m.decode('utf-8')
    print(f'from server: {m1}')
##    s.close()
    
