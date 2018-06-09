from socket import *
#创建udp
s = socket(AF_INET,SOCK_DGRAM)
conent = "1:234325435:lw:lw-pc:32:hhah"
s.sendto(conent.encode("gb2312"),("192.168.56.1",2222))
s.close()
