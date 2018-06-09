import os
file_name = input("请输入文件夹名字")
files = os.listdir(file_name)
for file in files:
    old_file_name= file_name+'/'+file
    new_file_name = file_name +'/'+'fff'+file
    os.rename(old_file_name,new_file_name)
