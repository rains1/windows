'''
登陆界面
'''
#空的购物车
gwc={}

def LandUI():
    bh=int(input("请输入编号："))
    if bh==1:
        #执行登陆的逻辑
        i=0
        while i<3:
            name = input("请输入用户名")
            password = input("请输入密码")
            if name == "张三" and password == "123":
                print("登陆成功")
                startUI()
                break
            else:
                print("登陆失败，请重新输入")
                print("你还有%d次机会"%(2-i))
            i+=1

    else :
        #退出程序
        pass


def startUI():
    print("-------欢迎进入手机淘宝-----")
    print("*****1  今日特卖******")
    print("*****2  女士服装******")
    print("*****3  男士服装******")
    print("*****4  美食茶酒******")
    print("*****5  结算******")
    bh=int(input("请输入编号："))
    if bh==1:
        #今日特卖
        jinriUI()

    elif bh==2:
        #女士服装
        pass
    elif bh == 3:
        # 男士服装
        pass
    elif bh == 4:
        # 美食
        pass
    elif bh ==5:
        # 结算
        jiesuan()
        pass


'''
今日特卖页面
'''
def jinriUI():
    print("****1  毛衫连衣裙  59元")
    print("****2  运动鞋  69元")
    print("****3  风衣  99元")
    bh=int(input("请输入要购买的商品编号："))
    if bh==1:
        #将商品信息存入到购物车（字典）中
        gwc["毛衫连衣裙"]=59
    elif bh==2:
        gwc["运动鞋"]=69
    elif bh==3:
        gwc["风衣"]=99

    print("购买成功，是否继续y/n")
    isY = input()
    if isY == "y":
        jinriUI()
    else:
        print("当前购物车商品信息有：")
        for k,v in gwc.items():
            print(k,v)
            # print("%s %d"%(k,v))
        startUI()

'''
结算
'''
def jiesuan():
    print("-------欢迎进入手机淘宝-----")
    print("您本次购买的商品列表如下：")
    for k,v in gwc.items():
        print(k,v)
    sum=0
    for v in gwc.values():
        sum+=v
    print("您本次消费：%d"%sum)
    gwc.clear()
    print("感谢使用手机淘宝，继续购物w退出0")
    isW=input()
    if isW=="w":
        startUI()
    else:
        print("退出")




print("-------欢迎进入手机淘宝-----")
print("1.登陆")
print("2：退出")
LandUI()
