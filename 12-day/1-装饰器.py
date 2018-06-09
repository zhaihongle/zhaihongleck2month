def test(fun):
    def inner():
        print("验证")
        fun()
    return inner 
@test
def f1():
    print("略略略")
xx()
