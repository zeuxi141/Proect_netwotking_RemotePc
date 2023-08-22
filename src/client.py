from socket import *

# s = socket.socket(addr_family, type)

# socket.AF_INET//ipv4
# socket.AF_INET6//ipv6

# socket.SOCK_STREAM //TCP
# socket.SOCK_DGRAM //UDP

#o day ta se chon ipv4 va TCP


s = socket(AF_INET, SOCK_STREAM)
s.connect(("192.168.1.14", 9000))
s.send()









