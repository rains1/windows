'''
编写程序，生成包含1000个0到100之间的随机整数，
并统计每个元素的出现次数

'''

#导入随机数的模块
# import random
#
# list=[]
#
# #生成随机数并添加到列表中
# i=1
# while i<=1000:
#     a=random.randint(0,100)
#     #将生成的随机数添加到列表中
#     list.append(a)
#     i+=1
#
#
# #找出现的次数
# for j in range(0,101):
#     b=list.count(j)
#     print("%d出现的次数%d"%(j,b))


'''
编写程序，用户输入一个列表和2个整数作为下标，
然后使用切片获取并输出列表中介于2个下标之间的
元素组成的子列表。例如用户输入[1, 2, 3, 4, 5, 6]和2,5，
程序输出[3, 4, 5]
'''
#a是一个字符串
# a=input("请输入列表：")
#
# #拆分字符串 列表中存储的是字符串类型的数据
# list=a.split(",")
# #存的是int类型的数据
# list1=[]
# #将list中字符串类型的数据转换成int类型存储到list1中
# for i in list:
#     j=int(i)
#     list1.append(j)
#
# xb1=int(input("请输入第一个下标："))
# xb2=int(input("请输入第二个下标："))
#
# list2=list1[xb1:xb2]
# print(list2)


'''
写一个存书的方法，当用户输入编号和书名，
将编号和书名存入到字典中，当用户输入over
的时候就提示：书添加成功，本次录入完毕。
写一个查书的方法，用户输入一个编号就输出对应的书名，
如果这个编号不存在就提示没有这本书
'''
#创建一个字典，将来存储书的编号和书名
dic={}
#存书的方法
def cun():
    while True:
        bh = input("请输入书的编号：")
        if bh == "over":
            print("录入完毕")
            break
        name = input("请输入书名")
        dic[bh] = name

#查书
def find():

   while True:
       bh = input("请输入你要查找的书的编号：")
       if bh in dic.keys():
           print("书名是：%s" % (dic[bh]))
       else:
           print("没有这本书")


cun()
find()

