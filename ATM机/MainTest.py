'''
用户：User
    属性：名字、手机号、身份证号、卡
    行为：
卡：Card
    属性：卡号、密码、余额、是否锁定(True锁定了False未锁定)
    行为：
ATM:
    属性：用户列表（存储所有开卡人的信息的）
    行为：开户、查询、存款、取款、转账、改密、锁定、解锁、销户、退出
管理员：Admin
    属性：用户名、密码
    行为：登陆
'''

from admin import Admin
from atm import ATM

def main():
    #1.创建管理员对象
    ad=Admin("admin",123)
    #2.管理员登陆
    ad.landUI()
    #3.创建ATM对象
    atm=ATM()
    #4.调用打印操作界面的函数
    while True:
        atm.printOptionUI()
        # 5用户输入对应的编号，调用对应的函数
        bh = input("请输入编号：")
        if bh == "1":
            # 开户
            atm.createUser()
        elif bh == "2":
            # 查询
            pass
        elif bh == "3":
            # 存款
            pass
        elif bh == "4":
            # 取款
            pass


if __name__=="__main__":
    main()