print("选项：")
print ("1.添加学员姓名")
print ("2.修改学员姓名")
print ("3.查询学员姓名: 1.查询单个学员 2.查询所有学员")
print ("4.删除学员姓名: 1.按序号删除 2.按名称删除 3.删除所有")
print ("0.退出程序")
a = ["小红","小明","小白","小强","小刚"]
while True:
    b = int(input())
    if b == 1:
        c = input('输入要添加的姓名：')
        a.append(c)
        print (a)
    elif b == 2:
        c = int(input("输入学员的序号："))
        d = input("输入修改信息：")
        a[c] = d
        print (a)
    elif b == 3:
        e = int(input("请输入查询方式:"))
        if e == 1:
            c = int(input("输入学员序号："))
            print (a[c])
        elif e == 2:
            for i in range(len(a)):
                print (a[i])
    elif b == 4:
        e = int(input("请输入删除方式:"))
        if e == 1:
            c = input("输入要删除的学员序号：")
            del a[c]
            print (a)
        elif e == 2:
            c = input("输入要删除的学员姓名：")
            a.remove(c)
            print (a)
        elif e == 3:
            del a
    elif b == 0:
        print ("退出程序")
        break

