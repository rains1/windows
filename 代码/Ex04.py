'''daoLength = int(input("请输入刀子的长度："))
if daoLength < 10:
    print("可以进站")
else:
    print("不可以进站")
chePiao = int(input("请出示车票："))
if chePiao > 2:
    print("可以上车")
    zuoWei = int(input("请输入座位数"))
    if zuoWei > 0:
        print("可以坐下")
    else:
        print("站着")
else:
    print("不能上车")
import random
player = int(input("请输入：剪刀（0）石头（1）布（2）"))
computer = random.randint(0,2)
#print("%d,%d"%(player,computer))
if ((player == 0) and (computer == 2)) or ((player == 1) and (computer == 0)) or((player == 2) and (computer == 1)):
    print("恭喜你，你赢了！")
elif player == computer:
    print("平局")
else:
    print("很遗憾你输了")
import random
count = 0
n = 0
playerCount = 0
computerCount = 0
while count < 3:
    player = int(input("请输入：剪刀（0）石头（1）布（2）"))
    computer = random.randint(0,2)
    if ((player == 0) and (computer == 2)) or ((player == 1) and (computer == 0)) or((player == 2) and (computer == 1)):
        playerCount += 1
        if playerCount == 2:
            print("恭喜你，你赢了")
            break
    elif player == computer:
        n += 1
        if n == 3 or playerCount == 1:
            print("平局")
    else:        
        computerCount += 1
        if computerCount == 2:
            print("很遗憾，你输了")
            break
    count += 1
print("END")
a = 1
#外层循环   控制打印的行数
while a <= 5:
    #内层循环  控制打印的次数
    b = 1
    while b <= 5:
        print("*",end='')
        b += 1
    print()
    a += 1
a = 1
#外层循环   控制打印的行数
while a <= 9:
    #内层循环  控制打印的次数
    b = 1
    while b <= a:
        print("%d*%d=%d"%(a,b,a*b),end='\t')
        b += 1
    print("\n")
    a += 1
a = 1
while a <= 3:
    print("你是一个好人....")
    a += 1
else:
    print("你很棒...")
x = 5
y = 5
for temp in range(x):
    for temp1 in range(y):
        print("*",end='')
    print("")
x = 0
for x in range(1,10):
    for y in range(1,x+1):
        print("%d*%d=%d"%(x,y,x*y),end='\t')
    print("\n")
year = int(input("请输入年份："))
if ((year % 4 == 0) and (year % 100 != 0)) or ((year % 100 == 0) and (year % 400 == 0)):
    print ("您输入%d年是闰年"%year)
else:
    print("您输入%d年不是闰年"%year)
#x = int(input("请输入打印的行数"))
#y = int(input("请输入打印的列数"))
n=10
m=n
for x in range(1,n+1):
        for y in range(1,x+1):
            print('*',end='')
        print('\n',end='')
for w in range(n+1,2*n):
        for q in range(1,m):
                print('*',end='')
        m-=1
        print('\n',end='')

n = int(input("请输入一个整数"))
for x in range(1,n):
    for y in range(1,x+1):
        print("*",end='')
    print("")
for w in range(n):
     for h in range(n):
         print("*",end='')
     n -= 1
     print("")
n = int(input("请输入一个整数"))
a = 1
while a <= n:
    b = 1
    while b <= a:
        print("*",end='')
        b += 1
    print("")
    a += 1
c = n-1
while c > 0:
    d = 1
    while d <= c:
        print("*",end='')
        d += 1
    print("")
    c -= 1
'''
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
a = my_abs(-1)
print(a)
