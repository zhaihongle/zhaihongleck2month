__all__=[]#如果本文件有函数不想被作为模块调用 就不要写在列表里  
          #列表里写的是作为模块被调用的函数名字






def test():
    print("我是小猪佩琪")
#test()  这样自己检查 在boss作为模块会被再次调用   boss 会出现两次结果
#正确自己检测：

if __name__ == "__main__":
    test()