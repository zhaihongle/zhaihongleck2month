from socket import *

s = socket(AF_INET,SOCK_STREAM)

s.connect(("192.168.19.119",6655))
s.send("烦烦烦".encode("gb2312"))
s.close()