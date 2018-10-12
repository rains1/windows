class Car:

    def __init__(self):
        self.oil=100
        self.speed=20
        print("新车上路")
    def show(self):

        print("当前时速%d，油量%d"%(self.speed,self.oil))
    def zhuan(self):
        print("汽车转弯")
        self.speed=20
        self.oil-=1
        self.show()
    def zhi(self):
        print("汽车直行加速")
        self.speed+=10
        self.oil-=1
        self.show()
    # def stop(self):
    #     print("停车")
    def __del__(self):
        print("停车")


c=Car()
c.zhi()
c.zhi()
c.zhuan()
c.zhi()
# c.stop()
