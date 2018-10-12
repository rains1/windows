'''
filter:
    过滤数据
    把列表中的每一个元素作用到函数中，符合条件True不符合False
    最终会把符合条件的数据存储到一个新列表
'''
list1=[1,2,3,4,5]
def oushu(x):
    if x%2==0:
        return x

list2=filter(oushu,list1)
print(list(list2))
# list2=[]
# for i in list1:
#     if i%2==0:
#         list2.append(i)
# print(list2)