def Decorator(der = 0):
    def decorator(fun):
        def inner(*args,**kwargs):
            if der == 1:
                return "I'm %d"%(args) + fun(*args,**kwargs) 
            if der == 2:
                print(fun(*args,**kwargs)) 
                return "yes"
        return inner
    return decorator 
@Decorator(1)
def test(*args,**kwargs):
    return "I am shuiguo " 
@Decorator(2)
def test1(*args,**kwargs):
    return "I am shuiguo ?" 
print(test(18))
print(test1())
