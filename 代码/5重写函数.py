'''
重写：再写一遍
1.重写__str__()
2.重写__repr__()
重写__str__()函数的作用：就是为了打印信息的
    在打印对象名字的时候其实就是在调用__str__()函数
repr函数和str的作用是一样的：只有当str不存在的时候
才会调用repr函数。如果2个函数都存在那么执行的是str函数
repr其实是系统调用的函数，在终端会调用repr函数
'''
class Person:
    def __init__(self,name,age,height,weight,sex):
        self.name=name
        self.age=age
        self.sex=sex
        self.height=height
        self.weight=weight

    def __repr__(self):
        return "呵呵"

    def __str__(self):
        return "姓名%s年龄%d性别%s身高%.1f体重%.1f"\
               %(self.name,self.age,self.sex,self.height,
                 self.weight)



#创建对象
#p1是对象，也叫作变量名
#Person()其实就是在调用构造函数
# p1=Person("张三",18,175,70,"男")
# print("姓名%s年龄%d性别%s身高%.1f体重%.1f"%(p1.name,p1.age,p1.sex,p1.height,p1.weight))
# p2=Person("李四",18,175,70,"男")
# print("姓名%s年龄%d性别%s身高%.1f体重%.1f"%(p2.name,p2.age,p2.sex,p2.height,p2.weight))

#当打印对象名的时候不打印地址值，打印的是对象的信息
p1=Person("张三",18,175,70,"男")
print(p1.__str__())
p2=Person("李四",18,175,70,"男")
print(p2)