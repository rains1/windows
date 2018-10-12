import os

#获取当前文件所在的路径
print(os.getcwd())

#获取指定的路径下所有的文件名字，保存在列表中
path=r"/Users/yang/Desktop/qianfeng/A"
print(os.listdir(path))

#创建一层
# os.mkdir("/Users/yang/Desktop/qianfeng/A/osDir")
#创建多层
# os.makedirs("/Users/yang/Desktop/qianfeng/A/osDir/dir1/dir2")

#删除一层
# os.rmdir("/Users/yang/Desktop/qianfeng/A/osDir/dir1/dir2")
#删除多层
# os.removedirs("/Users/yang/Desktop/qianfeng/A/osDir")

# os.rename("osDir","aaa")

#绝对路径  相对路径

#相对路径转绝对路径
# path="aaa"
# print(os.path.abspath(path))

#将文件和路径拆分并保存到元组中
# path=r"/Users/yang/Desktop/qianfeng/A/1循环.py"
# print(os.path.split(path))

#合并路径
# a=r"/Users/yang/Desktop/qianfeng/A"
# b="1循环.py"
# print(os.path.join(a,b))

#拆后缀
# path = '/home/sy/000.py'
# result = os.path.splitext(path)
# print(result)

#获取文件的大小
# print(os.path.getsize("aaa"))
# 获取文件的创建时间  毫秒值（时间戳）
# print(os.path.getctime("aaa"))

#判断是否是文件
# path =r"/Users/yang/Desktop/qianfeng/A/1循环.py"
# result = os.path.isfile(path)
# print(result)

#判断是否是文件夹
# path =r"/Users/yang/Desktop/qianfeng/A"
# result = os.path.isdir(path)
# print(result)

#检测某个路径是否存在
# filepath = '/Users/yang/Desktop/爱上讲的是'
# result = os.path.exists(filepath)
# print(result)

#检测是否是绝对路径
# path = '/Users/yang/Documents/PycharmProjects/untitled/ClassWork/aaa'
# result = os.path.isabs(path)
# print(result)

