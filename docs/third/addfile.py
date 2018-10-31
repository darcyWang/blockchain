#!/bin/python3


# import os

# for file in os.listdir('.'):    #os.listdir('.')遍历文件夹内的每个文件名，并返回一个包含文件名的list
#     if file[-2: ] == 'py':
#         continue   #过滤掉改名的.py文件
#     name = file.replace('-', '')   #去掉空格
#     new_name = name[-7:]   #选择名字中需要保留的部分
#     os.rename(file, new_name)


for i in range(1,15):
    if len(str(i)) == 2:
        print(str(i))
    else:
        print("0"+str(i))


for x in range(1,32):
    if len(str(x)) == 2:
        f = open("2018_12_"+str(x)+".md", 'w')
    else:
        f = open("2018_12_0"+str(x)+".md", 'w')

    
    # f.write(str(x) + "\n" + str(20-x))
    f.close()