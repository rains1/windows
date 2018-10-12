'''
构造函数：就是为了初始化赋值用的
'''

class Person:



    #构造函数
    def __init__(self,name,age):
        #要写对象的属性就在构造函数中用self去创建
        #谁点的self就是谁
        self.name=name
        self.age=age

    def show(self):
        print("姓名：%s"%self.name)


#当创建对象的时候会自动调用构造函数(__init__())
p1=Person("张三",18)
p1.name="李四"
p1.show()

p2=Person("aa",30)
p2.show()


print(Person.name)
