'''
人开枪射击子弹
类：
    人：Person
        属性：枪
        行为：开枪  装弹
    枪：Gun
        属性：弹夹
        行为：发射
    弹夹：
        属性：子弹数量
        行为：
'''

class DanJia:
    def __init__(self,bulletCount):
        self.bulletCount=bulletCount

class Gun:
    def __init__(self,danjia):
        self.danjia=danjia
    def shoot(self):
        #子弹数量减少
        if self.danjia.bulletCount<=0:
            #添加子弹  装弹
            print("该装弹了")
            pass
        else:
            self.danjia.bulletCount -= 1
            print("发射子弹，剩余数量%d" % self.danjia.bulletCount)

class Person:
    def __init__(self,gun):
        self.gun=gun

    def fire(self):
        #枪发射子弹
        self.gun.shoot()

#创建弹夹
dj=DanJia(5)
#创建一把枪
g=Gun(dj)
#创建一个人
p1=Person(g)
p1.fire()
p1.fire()
p1.fire()
p1.fire()
p1.fire()
p1.fire()
