import socket
s=socket.socket()
print('server started..')
port=1234
h=socket.gethostname()
s.connect((h,port))
while True:
    m=s.recv(1000)
    m1=m.decode('utf-8')
    print(f'from server: {m1}')
    msg=str(input('text something: '))
    s.send(msg.encode('utf-8'))
##s.close()
