'''
嵌套函数
'''

# def outer():
#     x=1
#     def inner():
#         print(x)
#     return inner()
#
# outer()


def outer(f):#mySum
    def inner(x,y):
        print("******")
        f(x,y)#mySum(1,2)
        print("******")
    return inner

@outer
def mySum(x,y):
    print("2数之和：",(x+y))

# aa=outer(mySum)#inner
# aa(10,20)#inner()
mySum(10,20)