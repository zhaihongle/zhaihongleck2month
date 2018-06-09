def fib():
    i = 0
    z,b = 0,1
    while i <9:
        #print(b)
        yield b
        z,b= b,z+b
        i+=1
b = fib()
next(b)
