import send
send.test()


#这种导入调用需要加模块的名字
#import send
#send.test()

#这种导入调用不需要加模块名字
#from send import test,oushu

#test()
#oushu()

#这种导入模块，如果多个模块里面函数名字相同，后面的导入会覆盖前面的
from send import *
test()
