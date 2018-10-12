'''name = input("请输入姓名：")
QQnumber = input("请输入QQ号：")
Phonenumber = input("请输入手机号：")
dress = input("请输入公司地址:")
print("============================")
print("姓名:%s\nQQ:%s\n手机号:%s\n公司地址:%s"%(name,QQnumber,Phonenumber,dress))
print("============================")
userNumber = input("请输入用户名：")
passWord = input("请输入密码：")
if"Admir" == userNumber and "123" == passWord:
    print("亲爱的xxx 欢迎登陆爱学习管理系统")
else:
    print("用户名或者密码错误")
print("===============================")
print("=   欢迎进入到身份认证系统V1.0\n=1.登录\n=2.退出\n=3.认证\n=4.修改密码")
print("================================")
'''
计算一元二次方程的根
import  math
def move(a, b, c):
    if a == 0:
        x = -c / b
        print("次方程只有一个根:%d" % x)
        return x
    else:
        if b ** 2 - 4 * a * c == 0:
            x = y = -b / 2 * a
            print("此方程有两个相等根")
            return x, y
        elif b ** 2 - 4 * a * c < 0:
            print("次方程无实数根")

        else:
            d = b ** 2 - 4 * a * c
            x = math.sqrt(d) / (2 * a) - b
            y = -(math.sqrt(d) / (2 * a) + b)
            print("次方程有两个根:%d,%d" % (x, y))
            return x, y


a = int(input(":"))
b = int(input(":"))
c = int(input(":"))
h = move(a, b, c)
print(h)
