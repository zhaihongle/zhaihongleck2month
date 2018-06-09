def  test1 ():
    print(nujm)

def  test2 ():
    test1()
def test3 ():
    try:
        test2()
    except Exception as ret:
        print(ret)
test3()
