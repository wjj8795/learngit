i = 1
while i == 1:
    km = int(input())
    if km <= 0:
        print ("请输入正确的公里数进行计算，程序结束")
    elif km > 0 and km <=2:
        money = 8
        print (money)
    elif km >2 and km <=12:
        money = 8 + (km - 2) * 1.2
        print (money)
    elif km > 12:
        money = 8 + 10 * 1.2 + (km - 12) * 1.5
        print (money)

