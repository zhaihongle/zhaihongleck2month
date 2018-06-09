#打印菜单
cards = []#定义空列表
def print_menu():
    print("名片管理系统v2.0".center(30,"*"))
    print("1:新增名片".center(30," "))
    print("2:查询名片".center(30," "))
    print("3:修改名片".center(30," "))
    print("4:删除名片".center(30," "))
    print("5:全部名片".center(30," "))
    print("6:退出系统".center(30," "))
#保存名片
def save():
    with open ("card.data","w") as f:
        f.write(str(cards))
#读取名片
def readc():
    global cards
    try:
        with open ("card.data","r") as f:
            cards = eval(f.read())
    except FileNotFoundError:
        pass


#分发功能模块
def input_fun():
    while True:
        fun_num = int(input("请选择功能"))
        if fun_num == 1:
            add_card()
        elif fun_num == 2:
            find_card()
        elif fun_num == 3:
            update_card()
        elif fun_num == 4:
            del_card()
        elif fun_num == 5:
            all_card()
        else:
            break
#新增名片
def add_card():
    card = {}
    name = input("请输入名字")
    job = input("请输入职位")
    company = input("请输入公司")
    phone = int(input("请输入手机号"))
    card["name"] = name
    card["job"] = job
    card["company"] = company
    card["phone"] = phone
    cards.append(card)
    print("添加成功")
    save()

def find_card():
    name = input("请输入要查的名字")
    flag = 0 #假设没有
    for temp in cards:
        if name == temp["name"]:
            print("名字:%s\n工作:%s\n公司:%s\n电话:%d\n"%(temp["name"],temp["job"],temp["company"],temp["phone"]))
            flag = 1
    if flag == 0:
        print("查无此人")
#修改名片
def update_card():
    name = input("请输入要修改的名字")
    flag = 0 #默认没有
    for temp in cards:
        if name == temp["name"]:
            flag = 1
            print("1:修改名字")
            print("2:修改职位")
            print("3:修改公司")
            print("4:修改手机")
            update_num = int(input("请输入要修改的选项"))
            if update_num == 1:
                new_name = input("请输入新的名字")  
                temp["name"] = new_name
            elif update_num == 2:
                new_job = input("请输入新的职位")
                temp["job"] = new_job
            elif update_num == 3:
                new_company = input("请输入新的公司")
                temp["company"] = new_company
            elif update_num == 4:
                new_phone = int(input("请输入新的手机号"))
                temp["phone"] = new_phone
            else:
                print("input is error")
    if flag == 0:
        print("没有此人")
#删除名片
def del_card():
    name = input("请选择删除的名字")
    flag = 0 #假设没有
    for temp in cards:
        if name == temp["name"]:
            flag = 1
            cards.remove(temp)
    if flag == 0:
        print("没有此人")
#打印名片
def all_card():
    print("名字".center(8," "),end=" ")
    print("职位".center(8," "),end=" ")
    print("公司".center(8," "),end=" ")
    print("手机号".center(8," "))

    for temp in cards:
        print(temp["name"].center(8," "),end = " ")
        print(temp["job"].center(8," "),end = " ")
        print(temp["company"].center(8," "),end = " ")
        print(str(temp["phone"]).center(13," "))
        #print("%s\t%s\t%s\t%d"%(temp["name"],temp["job"],temp["company"],temp["phone"]))       


readc()
print_menu()
input_fun()
