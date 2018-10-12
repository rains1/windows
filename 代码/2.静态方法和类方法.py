'''
静态方法：当函数不需要使用self点的一些东西的就给他编程静态函数
    在调用的时候通过类名直接调用
类方法：
实例（对象）方法：
'''

class Cat:
    age=10
    def __init__(self,name):
        self.name=name

    def eat(self):
        print("吃饭",self.name)
        print(Cat.age)

    @staticmethod
    def fun1():
        print('喜欢你')
    @classmethod
    def fun2(cls):
        print(cls.age)

c=Cat("a")
print(c.name)
print('**************')
Cat.fun1()
c.fun1()
print('**************')
Cat.fun2()
# Cat.eat(c)


# def aa():
#     pass
# 
# 
# class Tools:
# 
#     def MySum(self,x,y):
#         return x+y
# 
# # print(Tools.MySum(1,2))
# t=Tools()
# t.MySum(1,2)