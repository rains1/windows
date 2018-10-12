from user import User
import  sys


def main():
   while True:
       name = input("请输入用户名：")
       if name[0] >= "a" and name[0] <= "z":
          while True:
              password = input("请输入密码：")
              if len(password) >= 6:
                 while True:
                     sex = input("请输入性别：")
                     if sex == "男" or sex == "女":
                         u = User(name, password, sex)
                         u.show()
                         sys.exit()
                     else:
                         print("性别不合法")

              else:
                  print("密码长度不能小于6")

       else:
           print("用户名必须以字母开头，请重新输入")


if __name__=="__main__":
    main()

