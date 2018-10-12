'''
可迭代对象：可以直接作用于for循环的对象统称为可迭代对象，
    比如：list dict tuple都是
可以使用isinstace()去检测是否是可迭代对象iterable
可以直接作用于for的数据类型一般分为2种：
    1.集合
    2.generator，包括生成器和带yile的generator函数
'''
from collections import Iterable
from collections import Iterator

print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance({},Iterable))
print(isinstance("",Iterable))
print(isinstance(1,Iterable))
'''
可以通过next()函数不断获取下一个元素，直到报错即为
获取完成，没有下一个元素了
列表、元组虽然是一个可迭代对象，但不是迭代器，需先转化
'''
l = (x for x in [23,4,5,64,3435])
print(type(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))

list1=[1,2,3,4,5]
list1_1=iter(list1)
print(next(list1_1))
'''
生成器
'''
def aaa(x):
    while True:
        x=x+1
        yield x

a=aaa(1)
print(next(a))
print(next(a))
print(next(a))