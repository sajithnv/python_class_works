import socket
s=socket.socket()
print('client started..')
port=1234
h=socket.gethostname()
s.connect((h,port))
while True:
    m1=input('Enter a string: ')
    ms1=m1.encode('utf-8')
    s.send(ms1)
    m2=s.recv(1000)
    ms2=m2.decode('utf-8')
    print('result: ',ms2)
