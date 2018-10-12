'''
ATM:
    属性：用户列表（存储所有开卡人的信息的）
    行为：开户、查询、存款、取款、转账、改密、锁定、解锁、销户、
'''
import random
from card import Card
from user import User

class ATM:

    def __init__(self):
        self.user_dic={}

    def printOptionUI(self):
        print("************************************")
        print("*      开户(1)     查询(2)           *")
        print("*      取款(3)     存款(4)           *")
        print("*      转账(5)     改密(6)           *")
        print("*      锁定(7)     解锁(8)           *")
        print("*      销户(9)     退出(t)           *")
        print("************************************")

    def createUser(self):
        '''
        1.提示输入姓名、身份证号、手机号、2次密码、存款金额
        2.判断2次密码是否一致，不一致：开户失败，回到主界面
        :return:
        '''
        name=input("请输入姓名：")
        id=input("请输入身份证号：")
        phone=input("请输入手机号：")
        passwd1=input("请输入密码：")
        passwd2=input("请再次输入密码：")
        if passwd1!=passwd2:
            print("2次密码不一致，开户失败。。。")
            return False
        money=int(input("请输入存款金额，不得低于10："))
        if money<10:
            print("钱太少了，开户失败。。。。")
            return False
        #证明前面输入的信息都没有问题，可以开户
        #随机一个卡号(6)
        cardNum=""
        for i in range(6):
            a = random.randint(0, 10)
            cardNum+=str(a)
        #创建卡对象
        card=Card(cardNum,passwd1,money)
        #创建用户对象
        user=User(name,phone,id,card)
        self.user_dic[cardNum]=user
        print("开户成功！！！卡号是：%s"%cardNum)
