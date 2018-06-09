def decorator(fun):
    def inner(*args,**kwargs):
        print(*args)
        print(str(*args),end='') 
        fun(*args,**kwargs) 
    return inner
@decorator
def test(*args,**kwargs):
    print( "I am shuiguo " )

test(18)
