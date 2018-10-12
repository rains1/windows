class User:

    def __init__(self,name,password,sex):
        self.name=name
        self.password=password
        self.sex=sex

    def show(self,):
        print("姓名：%s 密码：%s 性别：%s"%(self.name,
                                   self.password,
                                   self.sex))