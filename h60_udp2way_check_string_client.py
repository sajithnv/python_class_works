import socket
s=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
print('socket started..')
port=1234
h=socket.gethostname()
i=(h,port)
print('client started..')
while True:
    m1=input('Enter anything : ')
    ms1=m1.encode('utf-8')
    s.sendto(ms1,i)
    c,addr=s.recvfrom(1000)
    m2=c.decode('utf-8')
    print(m2)
    
