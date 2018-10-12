'''
sorted:
    排序
'''

list1=[90,7,0,2,1,-3,-8]
# list1.sort() 会修改原列表
# print(list1)
#升序
list2=sorted(list1)
print(list1)
print(list2)
#降序True  默认是False升序
list3=sorted(list1,reverse=True)
print(list3)

list4=sorted(list1,key=abs)
print(list4)


list5=["asd","sfef","aa"]
list6=sorted(list5,key=len)
print(list6)