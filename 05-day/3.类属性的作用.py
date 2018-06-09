class Dog():
    count = 0
    def __init__(self,name):
        self.name = name
        Dog.count+=1
taidi = Dog("泰迪")
hashiqi = Dog("哈士奇")
print(Dog.count)
