'''
析构函数：
    在对象销毁的时候默认执行的
    对象销毁时间：1.程序执行完毕的时候就自动销毁
                2.自己手动销毁，用del销毁
                3.如果变量写在函数内部，那么函数执行完毕
                  变量会自动销毁
    注意：对象（变量）销毁了就不能再使用了，再使用会报错
'''

class Person:

    def __init__(self):
        print("出生了")
        self.name=""
    #析构函数
    def __del__(self):
        print('我死了')


# p1=Person()
# p1.name="张三"
# print(p1.name)
#
# for i in range(10):
#     if i==7:
#         #销毁p1
#         del p1
#         continue
#     print(i)
#
# print(p1.name)
import  time
def fun():
    print('函数开始执行')
    p1=Person()
    time.sleep(3)
    print('函数执行完毕')


fun()
for i in range(10):
    print(i)