import socket
s=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
print('client Strated..')
port=1234
h=socket.gethostname()
i=(h,port)
while True:
    msg2=input('msg content: ')
    m2=msg2.encode('utf-8')
    s.sendto(m2,i)
    
