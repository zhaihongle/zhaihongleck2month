from socket import * 
from threading import Thread
s =""
newsocket = None
def recv():	
	while True:
		recvdata = newsocket.recv(1024)
		if len(recvdata)>0:
			print(recvdata.decode("gb2312"))
		else:
			break
def send():
	while True:
		newsocket.send("hahah".decode("gb2312"))
def main ():
	global s
	global newsocket
	s = socket(AF_INET,SOCK_STREAM)
	s.bind(("",11223))
	s.listen(5)
	newsocket,infor = s.accept()
	t = Thread(target = send)
	t1 = Thread(target = recv)
	t.start()
	t1.start()
	t.join()
	t1.join()

	newsocket.close()
	s.close()
