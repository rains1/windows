'''
import random             # 随机生成0~100的数，猜三次
computer = random.randint(1,101)
i = 1
while i <= 3:
    player = int(input("请输入0-100之间的整数："))
    if player > computer:
        print("您猜的数字偏大了")
    elif player < computer:
        print("您猜的数字偏小了")
    else:
        print("恭喜您，猜对了！")
        break
    i += 1
print("GAME OVER")

# 从键盘上输入5个数，且当输入负数时结束，并且求其平均值
i = 1
sum = 0
count = 0
while i <= 5:
    a = int(input("请输入一个数"))
    if a > 0:
        sum += a
        count += 1
    elif a < 0:
        print("您输入错误，结束输入！")
        break
    i += 1
average = sum / count
print("您所输入的%d个数的平均值为：%f"%(count,average))

#珠穆朗玛峰高8848M，一张纸厚0.01M，请问折叠多少次，厚度不低于珠穆朗玛峰的高度
Hight = 1
count = 0
while Hight <= 884800:
    count += 1
    Hight = Hight * 2
print ("需要折叠%d次"%count)
'''
#小芳每天存2.5，当今天是存钱的第五天或者5的倍数的话，她会花6元，经过多少天才可以存到100元。
day = 0
Money = 0
while Money <= 100:
    day += 1
    Money += 2.5
    if day % 5 == 0:
        Money = Money - 6
print("需要存%d天"%day)
