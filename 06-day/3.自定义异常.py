class ShowError(Exception):
    def __init__(self,len,length):
        self.len = len
        self.length = length
def main():
    try:
        s = input("dddd")
        if len(s) <3:
            raise ShowError(len(s),3)
    except ShowError as ret:
        print(ret)
        print("ShowError:输入是%d,长度至少是%d"%(ret.len,ret.length))
main()
