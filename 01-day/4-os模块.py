import os
oidfile = input('文件名')
files = os.chdir(oidfile)
for file in files:
    old_file = oidfile+'/'+file
    position = files.rfind(".")
    new_file = oidfile[0:positioin]+"l乐"+oidfile[position:]
    os.rename(old_file,new_file)
