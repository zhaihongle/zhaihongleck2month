class Dog:
    global name
    def wangwangjiao(self):
        print(name+'汪汪叫')
    def yaoweiba(self):
        print(name+'摇一摇尾巴说：主人好')
def object():
    name = Dog()
    name.wangwangjiao()
    name.yaoweiba()
name = input('名字')
object()
