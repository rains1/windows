a=20
b=21
c=20
d=23
e=24
a=20
b=21
c=22
d=23
e=24
a=20
b=21
c=22
d=23
e=24
a=20
b=21
c=22
d=23
e=24
print((a+b+c+d+e)/5)
#列表 可以看做是容器，可以存储多条数据
#创建一个列表 列表的标志是[]
list1=[20,21,30,22,23]
#访问列表中的数据
# num=0
# sum=0
# while num<4:
#     sum+=list1[num]
#     num+=1
#增删改查
#在尾部添加一个元素
# list1.append(24)
# list1.append(["a","b"])
# #在尾部添加多个元素（数据）
# list1.extend(["c","d"])
# list1.insert(2,"100")
# list1.pop(3)  #根据下标去删除，不写删除最后一个
# list1.remove(30)  #删除指定的元素
# list1.clear()      #清空

# list1[4]=230      #修改

#---------查--------
print(len(list1))  #输出列表中元素的个数
print(list1.index(30))   #查找元素所对应的下标
print(list1.count(12))     #某个元素出现的次数
print(list1)

list2=[10,6,1,2,3]
# list2.reverse()    #倒序输出
list2.sort()   #升序（从小到大）
print(list2)
print("---------------")
list10 = [1,2,3,4,5,6,7,8,9]
print(list10[2:6])
print(list10[3:])
print(list10[:5])
print("------------------")
# list11=[1,2,3]
# list12=list11
# list12[1]=20
# print("list11:",list11)
# print("list12:",list12)

a=10
b=a
b=20
print(a)
print(b)

#值类型（整数、小数、布尔）  引用类型

print("----------")
list11=[1,2,3]
list12=list11.copy()
list12[1]=20
print("list11:",list11)
print("list12:",list12)


# a=input("请输入数据")
# b=a.split(",")
# b.sort()
# print(b)
# b.reverse()
# print(b[1])

# a = input('输入数据：')
# l1=a.split(',') #存储的字符串的数据
# l = []
# num=0
# while num<len(l1):
#     b=int(l1[num])
#     l.append(b)
#     num+=1
# l.sort(reverse=True)
# print(l[1])

list3=["a","b","c"]
for i in  list3:
    print(i)
