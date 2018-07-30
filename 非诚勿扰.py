print ("请按顺序输入男生年龄、身高、体重、收入：")
year1,height1,weight1,income1 = input().split()
year1,height1,weight1,income1 = int(year1),int(height1),int(weight1),int(income1)
print ("请按顺序输入女生年龄、身高、体重、收入：")
year2,height2,weight2,income2 = input().split()
year2,height2,weight2,income2 = int(year2),int(height2),int(weight2),int(income2)
if year2 >= 20 and year2 <= 28 and height2 >= 160 and height2 <= 175 and weight2 >= 40 and weight2 <= 60 and income2 >= 2000 and income2 <= 5000:
   a = 1
if year1 >= 22 and year1 <= 30 and height1 >= 170 and height1 <= 185 and weight1 >= 55 and weight1 <= 80 and income1 >= 4000 and income1 <= 12000:
    b = 1
if a == b:
    print("配对成功")
else:
    print("配对失败")
