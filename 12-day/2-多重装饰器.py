def test(fun):
    def inner():
        return "%%%" + fun() + "%%%"
    return inner 
def test1(fun):
    def inner1():
        return "^^^^ "+ fun() + "^^^"
    return inner1 
@test1
@test # f1 = test(f1)
def f1():
    return "略略略"
print(f1())
