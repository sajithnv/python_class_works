import socket
s=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
print('Server Strated..')
port=1234
h=socket.gethostname()
s.bind((h,port))
print('socket Strated..')
while True:
    msg,addr=s.recvfrom(1000)
    m1=msg.decode('utf-8')
    print('from client: ',m1)
    msg2=input('msg content: ')
    m2=msg2.encode('utf-8')
    s.sendto(m2,addr)
    
