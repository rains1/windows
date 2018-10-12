'''
*是元组
**是字典
'''
def fun(*args,**kwargs):
    print(args)
    print(kwargs)
dic={"name":"a",
     "age":10}
fun(1,2,3,4,5,9,dic,x=1,y=2)