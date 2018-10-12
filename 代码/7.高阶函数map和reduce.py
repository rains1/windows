'''
map:
    需要传递2个参数，第一个参数：函数，第二个参数：序列
    会将序列中的每个元素依次拿出作用于函数上，
    再返回一个新的序列
reduce:
    将序列中的所有数据进行求和
'''

def myPow(x):
    return x*x

list1=[1,2,3,4,5]
list2=map(myPow,list1)
# list2=[]
# for i in list1:
#     a=myPow(i)
#     list2.append(a)
print(list2)
# print(list1)
print(list(list2))

# list3=map(str,list1)
# print(list(list3))
# list4=[]
# for i in list1:
#     a=str(i)
#     list4.append(a)
from functools import reduce

list5=["a","b","c","d","e"]
def add1(x,y):
    return x+y
str=reduce(add1,list5)
print(str)



list7=[1,2,3,4,5]
# print(sum(list7))
def add(x,y):
    return x+y #6
sum=reduce(add,list7)
print(sum)

#写一个列表，列表中存储几个字符串
#将字符串的首字母大写，其余小写