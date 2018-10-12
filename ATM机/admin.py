'''
管理员：Admin
    属性：用户名、密码
    行为：登陆
'''
import sys

class Admin:

    def __init__(self,name,passwd):
        self.name=name
        self.passwd=passwd

    def landUI(self):
        print("---------------------欢迎来到XXX银行------------------------")
        name=input("请输入管理员账号：")
        passwd=int(input("请输入管理员密码："))
        if name==self.name and passwd==self.passwd:
            print("！！！!登陆成功！！！！请稍后。。。。")
        else:
            print("账号或密码错误，登陆失败")
            sys.exit()