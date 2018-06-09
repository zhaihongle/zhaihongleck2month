import os
dir_name = input('请输入名字')
files = os.listdir(dir_name)
os.chdir(dir_name)
for file in dir_name:
    print(file)
    position = file.rfind('.')
    new_file_name = file[0:position]+'乐乐'+file[position:]
    os.rename(file,new_file_name)

