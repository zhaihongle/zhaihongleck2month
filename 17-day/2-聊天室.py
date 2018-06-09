from socket import* 
from threading import Thread


ip=""
port = 0
s = None
def send():
    while True:
        content = input("输入内容")
        s.sendto(content.encode("gb2312"),(ip,port))
def voce():
    while True:
        con = s.recvfrom(1024)
        print(\r"%s---%s"\n%(con[0].decode("gb2312"),con[1][0]),end="")
        


def main ():
    global ip 
    global port
    global s
    ip = input("输入IP地址")
    port = int(input("输入窗口"))
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(("",6666))
    t = Thread(target = send) 
    t1 = Thread(target = voce)
    t.start()
    t1.start()
    t.join()
    t1.join()
if __name__ == "__main__":
    main()
