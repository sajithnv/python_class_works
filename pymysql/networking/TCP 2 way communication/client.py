###client side
##import socket
##s=socket.socket()
##print('client started..')
##port=1234
##h=socket.gethostname()
##s.connect((h,port))
##m=s.recv(1000)
##m1=m.decode('utf-8')
##print(f'from server: {m1}')
##s.bind((h,port))
##print('socket created..')
##s.listen(3)
##while True:
##    c,addr=s.accept()
##    msg=input('text somthing: ')
##    c.send(msg.encode('utf-8'))
##s.close()
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
    msg=str(input('text somthing: '))
    c.send(msg.encode('utf-8'))
s.connect((h,port))
m=s.recv(1000)
m1=m.decode('utf-8')
print(f'from server: {m1}')
s.close()
    
