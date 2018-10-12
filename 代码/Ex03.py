'''chePiao = int(input("请输入0,1,0代表没有车票，1代表有车票")) # 1 代表有车票   0代表没有车票
if chePiao == 1:
    print("可以上车")
    zuoWei = int(input("请输入座位数量："))
    if zuoWei > 0:
        print("请坐下")
    else:
        print("站着")
else:
    print("不能上车")
import random
def caiQuan():
    p = int(input("请输入：剪刀（0）石头（1）布（2）"))
    c = random.randint(0,2)
    if ((p == 0) and (c == 2)) or ((p == 1) and (c == 0)) or ((p == 2) and (c == 1)):
        print("你赢了")
        return 1
    elif p == c:
        print("平局")
        return 0
    else:
        print("你输了")
        return -1
sum = 0
for x in range(3):
    n = caiQuan()
    if n == 1:
        sum += 1
    elif n == 0:
        sum += 0
    else:
        sum += -1
    if x == 1:
        if sum == 2:
            print("恭喜你，你赢了")
            break
        elif sum == -2:
            print("很遗憾，你输了")
            break
if sum == 1 or sum == 2:
    print("恭喜你，你赢了")
elif sum == 0:
    print("平局")
else:
    print("很遗憾，你输了")'''
i = 0
while i <= 5 :
    j = 0
    while j <= i:
        print("*",end="")
        j += 1
    print("")
    i += 1

i = 4
while i >= 0:
    j = 0
    while j <= i:
        print("*",end="")
        j += 1
    print("")
    i -= 1