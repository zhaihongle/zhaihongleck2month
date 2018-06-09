from socket import *
#coding = utf-8
#创建udp
s = socket(AF_INET,SOCK_DGRAM)
s.sendto("hehe".encode("gb2312"),("192.168.19.119",8080))
#while True:
    #a = s.recvfrom(1024)
   # print(a.decode("gb2312"))
s.close()
