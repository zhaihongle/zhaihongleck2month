
class A():
    def test(self):
        print("AAAAAAAAAAA")
class B(A):
    def test(self):
        super().test(self)
        print("BBBBBBBBBBBB")
b = B()
b.test()#这样写子类执行ＢＢＢＢＢＢ
