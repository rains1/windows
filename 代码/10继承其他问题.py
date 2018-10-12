class Person:

    '''
    构造函数有参数的情况
    子类必须给父亲构造函数赋值
    '''
    # def __init__(self,name,age):
    #     self.name=name
    #     self.age=age
    '''
    构造函数无参的
    子类也必须调用父亲的构造函数
    '''
    def __init__(self):
        self.name = ""
        self.age = 0
        print("父亲")

    def study(self):
        print("人学习")

class Student(Person):

    def __init__(self,id):
        # super(Student, self).__init__(name,age)
        Person.__init__(self)
        self.id=id
        print("儿子")


s1=Student(1001)
s1.age=10
s1.name="aaa"
print(s1.name,s1.age)
