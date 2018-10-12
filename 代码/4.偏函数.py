'''
偏函数：就是函数的辅佐
    固定函数里面的参数用的
    在原函数的基础上固定住一个参数再生成一个新函数
    不会更改原函数
使用：当一个参数的值一直需要重复使用的时候
'''

# def str2int(str):
#     return int(str,base=2)
#
#
# print(str2int("1010"))
# print(str2int("10101"))

import functools
#要固定那个函数的参数，就把那个函数名字写到第一个参数位置
str2int=functools.partial(int,base=8)
print(str2int("1010"))
print(str2int("10101"))


def mySum(x,y):
    return x+y

# print(mySum(1,2))
# print(mySum(1,3))
# print(mySum(1,4))
mySum2=functools.partial(mySum,2)
print(mySum2(2))
print(mySum2(3))
mysum3=functools.partial(mySum,3)
