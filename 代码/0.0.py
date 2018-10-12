'''
i = 1
sum1 = 0
sum2 = 0
while i <= 100:
    if i % 2 == 0:
        sum1 = sum1 + i
    else:
        sum2 = sum2 + i
    i += 1
print('100以内的奇数和为：%d'%sum1)
print('100以内的偶数和为：%d'%sum2)

i = 5
a = 1
while i > 0:
    a = i * a
    i -= 1
print(a)

i = 100
count = 0
l = []
while i <= 999:
    a = i // 100
    b = i // 10 % 10
    c = i % 10
    if a * a * a + b * b * b + c * c * c == i:
        print(i)
        l.append(i)
        count += 1
    i += 1
print(count)
print(l)
                
i = int(input('请输入一个整数'))
a = 1
while i > 0:
    a = i * a
    i -= 1
print(a)

i = 10000
count = 0
while i <= 99999:
    wanwei = i // 10000
    qianwei = i // 1000 % 10
    baiwei = i // 100 % 10
    shiwei = i // 10 % 10
    gewei = i % 10
    if gewei == wanwei and shiwei == qianwei and gewei + shiwei + qianwei + wanwei == baiwei :
        print (i)
        count += 1
    i += 1
print(count)

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d * %d = %d"%(i,j,i*j),end='\t')
        j += 1
    print("\n",end='')
    i += 1

i = 1
while i <= 5:
    g = 1
    while g < i:
        print(" ",end='')
        g += 1
    j = 5
    while j >= i:
        print("*",end='')
        j -= 1
    print()
    i += 1
'''
import random             # 随机生成0~100的数，猜三次
computer = random.randint(1,100)
i = 1
while i <= 3:
    player = int(input("请输入0-100之间的整数："))
    if player > computer:
        print("您猜的数字偏大了")
    elif player < computer:
        print("您猜的数字偏小了")
    else:
        print("恭喜您，猜对了！")
    i += 1
print("GAME OVER")
