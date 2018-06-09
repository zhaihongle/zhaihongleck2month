from time import ctime, sleep

def timefun(func):
    def wrappedfunc(a,b,**kwargs):
        print("%s called at %s"%(func.__name__, ctime()))
        func(a,b, **kwargs)
    return wrappedfunc

@timefun
def foo(a, b, **kwargs):
	for k,v in kwargs.items():
		print ('key=%s,value=%s'%(k,v))
		print(a+ b+ int(v))

foo(3,5,age = 7)
sleep(2)
foo(2,4,age = 9)
