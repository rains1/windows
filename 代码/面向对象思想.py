'''
面向对象：注重的是设计，从现实生活角度去考虑问题
        一切皆对象，只要是具体存在的看得见摸得着的东西
        全部都是对象
    好处：易于维护
    就是将同一类事物的变量和函数放到一个容器中
    容器怎么写呢？
        就是我们的类(class)
        类中可以写：变量和函数
    一个事物由属性和行为构成：
        属性：就是一个事物的信息
        行为：就是这个事物会做什么事情
    类是用来描述一个事物的，也就是说：
        类是由属性和行为构成的
            属性用变量表示
            行为用函数表示
        类是由变量和函数构成的

面向过程：注重的是结果,从结果出发考虑问题，
        中间实现过程不考虑，怎么实现都行
        我只要结果
    缺点：不易于维护

一辆车60/km,一条路总共1000km，问多久走完
'''
# speed=30
# distance=1000
# print(distance/speed)
'''
先写车(速度)
写条路(距离)
'''

'''
要求：设计一个植物大战僵尸的程序
'''

# def taiyang():
#     pass
#
# hp=100
# def fashe():
#     pass
# def yao():
#     pass
# hp1=200
# def eat():
#     pass
# def walk():
#     pass
#
# hp1=200
# def eat():
#     pass
# def walk():
#     pass
#

'''
面向对象设计植物大战僵尸
'''
class Flower:
    hp=100
    #生成太阳
    #在类中写的函数自带self参数
    def creat(self):
        print("向日葵生成太阳")


#创建豌豆射手类
class wdshooter:
    hp=200
    def fire(self):
        print("豌豆射手发射子弹")
    def yao(self):
        print("豌豆射手摇晃")

#创建普通僵尸类
class zombie:
    hp=50
    def eat(self):
        print("普通僵尸吃植物")
    def walk(self):
        print("普通僵尸走路")

'''
开始游戏
'''
#创建向日葵变量
#创建一个向日葵对象（实例化一个向日葵对象）
#创建对象格式：变量名=类名()
f=Flower()
f.creat()
f.hp=200
print("f的生命值%d"%f.hp)

f1=Flower()
print("f1的生命值：%d"%f1.hp)

'''
f和f1是对象，Flower是类
类和对象的关系：
    类是一个模板（可以看做是一个图纸）
    对象是根据图纸创建出来的一个作品
'''

'''
2只手交换卡牌
对象：2只手  2张卡牌
类：人  卡牌

人：
    属性：左手牌 右手牌 
    行为：抓拍  交换牌
牌：
    属性：花色  数字
    行为：
牌库：
手：
'''

class Person:
    left=""
    right=""
    def zhua(self,a,b):
        global left, right
        left=a
        right=b
        print(left,right)

    def huan(self):
        global left,right
        temp=left
        left=right
        right=temp
        print(left,right)


class Card:
    color=""
    num=""

'''
如果打印的是对象名的话结果是地址值
'''
#创建2张牌
c1=Card()
c1.color="♥"
c1.num="3"

c2=Card()
c2.color="♣"
c2.num="4"

#创建人的对象
p1=Person()
p1.zhua(c1.color+c1.num,c2.color+c2.num)
p1.huan()



