'''
回调函数：
    把一个函数当做参数传递给另一个函数
'''

# def fun1():
#     print("fun1")
#
# def fun2():
#     print("fun2")
#
# def run(f):
#     print("开始调用")
#     f() #10()
#     print("结束调用")
#
# run(fun1)

'''
写一个测试函数，当一调用这个测试函数的时候，可以传递
多个函数进去，比如：传递一个猫叫的函数和一个老鼠跑的函数
最终结果：当调用这个测试函数的时候就会输出猫叫、老鼠跑
'''
def run(*f):
    for i in f :
        i()

def cat_shout():
    print('猫叫')
def mouse_run():
    print("老鼠跑")

run(cat_shout,mouse_run)

