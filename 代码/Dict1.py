'''
字典：
    是一个键值对形式的集合
    字典没有下标
    字典是无序的，不重复的
    {}
'''
#创建字典
dict1={1:"a",
       2:"b",
       3:"c"}

print(type(dict1))
#访问字典
print(dict1[1])
dict1[2]="hello"
#增删改查
#添加
dict1[10]="world"


dict1.pop(2)
print(dict1) 

