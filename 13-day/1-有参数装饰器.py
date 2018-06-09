def decorator(fun):
    def inner(a,b):
        print("jieguoshi",end='')
        fun(a,b)
        print("")
    return inner
@decorator #test = de(test)
def test(a,b):
    print(a+b)
test(18,2)
