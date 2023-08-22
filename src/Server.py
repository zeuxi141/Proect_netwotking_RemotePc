from socket import *

s = socket(AF_INET, SOCK_STREAM)

s.bind(("192.168.1.14", 9000))

s.listen(5)

while True:
    c,a = s.accept()
    print ("recevied connection from", a)
    c.send("hello %s\n"%a[0])
    c.close()

