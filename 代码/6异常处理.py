'''
异常处理：
    代码报错了依然会执行后面的代码
    try...except..else
    try...except...finally
    else  和  finally可写可不写
    else:没有找到错误原因的时候执行
    finally：不管有没有错误都执行
'''
print("start")

# try:
#     print(3 / 1)
# except ZeroDivisionError as e:
#     print("除数不能为0")
# print("over")
#
# x=10
# try:
#     print(x + 1)
# except NameError as e:
#     print("变量未定义")
# print("over111")
x=0
try:
    print(3/x)
except ZeroDivisionError as e:
    print("除数不能为0")
except NameError as e:
    print("变量未定义")
finally:
    print("没有找到匹配的错误原因")

print("over")
