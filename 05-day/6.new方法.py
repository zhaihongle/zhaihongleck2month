class Tree():
    def __init__(self):
        self.name = "叔叔叔叔叔"
    
    def __new__(cls):
        return object.__new__(cls)
            #创建对象的时候　在object默认调用ｎｅｗ方法
            #现在是重写object的new方法


t = Tree()
print(t.name)

