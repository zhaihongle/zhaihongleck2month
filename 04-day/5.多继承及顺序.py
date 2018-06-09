class A():
    def test(self):
        print("---------------")
class B():
    def test(self):
        print("============")
class C(B,A):
    pass
c = C()
c.test()#如果多个父类方法一样按在子类继承时顺序
class A():
    def testa(self):
        print("---------------")
class B():
    def testb(self):
        print("============")
class C(A,B):
    pass
c = C()
c.testa()
c.testb()
