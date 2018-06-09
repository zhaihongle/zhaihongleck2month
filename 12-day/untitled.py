def foo(a, b, **kwargs):
	for k,v in kwargs.items():
		print ('key=%s,value=%s'%(k,v))
		print(a+ b+v)
foo(1,2,)
