'''
猜数字：
1.生成一个随机数 1-100
2.录入一个数据
3.拿录入的数据和随机的数据作比较  if
    输入的大于随机的提示：输入太大了
    输入的小于随机的提示：输入太小了
    等于提示：猜中了
4.加循环
'''

# import random
# a=random.choice(range(1,101))#随机1-100之间的数字
# #所有录入的数据都是字符串类型的
# num=1
# while num<=3:
#     b = input("请输入一个数字：")
#     # 把字符串b转换成数字类型
#     c = int(b)
#     if c > a:
#         print("输入太大了")
#     elif c < a:
#         print("输入太小了")
#     else:
#         print("猜中了")
#         break
#     num+=1

'''
输入5个数求平均值，如果输入的是负数就停止程序
1.定义一个次数的变量（循环的初始值）
2.循环语句
3.在循环体内写录入语句
4.拿录入的数据与0作比较，如果小于0就break
5.求平均分
'''
# num=1
# sum=0
# while num<=5:
#     score=int(input("请输入第%d个人的成绩"%num))
#     if score<0:
#         print("输入错误")
#         break
#     else:
#         sum+=score
#     if num>=5:
#         print("平均分%f" %(sum/5))
#     num += 1

'''
我国最高山峰是珠穆朗玛峰：8848m，我现在有一张足够大的纸张，
  厚度为：0.01m。请问，我折叠多少次，就可以保证厚度不低于珠
  穆朗玛峰的高度?1   884800
  
1.先定义纸的初始厚度
2.定义次数的变量
'''
# height=1
# count=0
# while True:
#     height=height*2
#     count+=1
#     if height>=884800:
#         break
# print("折叠%d次"%count)
#
# '''
# 小芳的妈妈每天给她2.5元钱，她都会存起来，但是，
#   每当这一天是存钱的第5天或者5的倍数的话，她都会花去6元钱，
#   请问，经过多少天，小芳才可以存到100元钱。74
# 1.定义钱的变量
# 2.定义天数变量
# 3.判断钱数大于等于100结束循环
# '''
# money=2.5
# day=1
# while True:
#     money+=2.5
#     day+=1
#     if day%5==0:
#         money-=6
#     if money>=100:
#         break
# print("天数",day)
# import sys
#
#
# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
fun1()