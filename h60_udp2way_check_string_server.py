import socket
s=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
print('socket started..')
port=1234
h=socket.gethostname()
s.bind((h,port))
print('server started..')
while True:
    c,addr=s.recvfrom(1000)
    m1=c.decode('utf-8')
    print('Received text is: ',m1)
    if m1.isdigit()==1:
        m2='Entered text have only digits..'
        ms2=m2.encode('utf-8')
        s.sendto(ms2,addr)
    if m1.isalpha()==1:
        m2='Entered text have only alphabets'
        ms2=m2.encode('utf-8')
        s.sendto(ms2,addr)
    else:
        m2=f'Entered text is: {m1}'
        ms2=m2.encode('utf-8')
        s.sendto(ms2,addr)
