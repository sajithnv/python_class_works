import socket
s=socket.socket()
print('server created..')
port=1234
h=socket.gethostname()
s.bind((h,port))
print('socket created..')
s.listen()
c,addr=s.accept()
while True:
    m1=c.recv(1000)
    ms1=m1.decode('utf-8')
    print('Recieved string is: ',ms1)
    s=ms1[::-1]
    print(s)    
    if s==ms1:
        m2='Entered string is pallindrome'
        ms2=m2.encode('utf-8')
        c.send(ms2)
    else:
        m2='Entered string is not pallindrome'
        ms2=m2.encode('utf-8')
        c.send(ms2)
        
    


