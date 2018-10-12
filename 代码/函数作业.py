s1="移动速度增加！攻击造成沉默！德玛西亚！"
s2="我是小陀螺，刷刷刷转起来"
f=100
#在函数内部定义的变量是局部变量，只能够在函数内部使用
#在函数外部定义的变量是全局变量，在哪都能使用,但是如果要在函数内部修改全局变量的值必须先用global引用
def shifang(s,xh):
    global f
    print(s)
    f-=xh
    print("当前法力值：%d"%f)

print("人在他在")
print("当前法力值：%d"%f)

while f>=0:
    print("请选择你要释放的技能1.德玛西亚2.小陀螺")
    bh = int(input())
    if bh == 1:
        shifang(s1, 10)
    else:
        if f>=20:
            shifang(s2, 20)
