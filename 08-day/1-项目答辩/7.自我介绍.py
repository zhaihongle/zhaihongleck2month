from time import sleep
class main(object):
	def __init__(self):
		self.name = "翟宏乐"
		self.age = "19"
		self.student = "北财学生"
		self.address = "河北张家口市"
	def __str__(self):
		msg = "姓名:%s\n年龄:%s\n职业:%s\n地址:%s"%(self.name,self.age,self.student,self.address)
		return msg
class onemonth(main):
	def clearn(self):
		print("hahah")

my = onemonth()
print(my)
sleep(0.5)
my.clearn()		