import json
import os
#
# dict={"name":"张三",
#       "age":10}
# f=open(os.path.join(os.getcwd(),"he.txt"),"w")
# # s=json.dumps(dict)
# # f.write(s)
# s=json.dump(dict,f)
# print(s)
# f.close()
#
# f1=open(os.path.join(os.getcwd(),"he.txt"),"r")
# dict1=json.load(f1)
# f1.close()
# print(dict1)

#
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age


# def Cat2Dic(st):
#     return {
#         "name":st.name,
#         "age":st.age
#     }
c1=Cat("hehe",10)
f = open(os.path.join(os.getcwd(),"he1.txt"),"w")
json.dump(c1,f,default=lambda obj:obj.__dict__)
f.close()

f1 = open(os.path.join(os.getcwd(),"he1.txt"),"r")
aa=json.load(f1)
print(aa)

#
# a=json.dumps(c1,default=Cat2Dic)
# a=json.dumps(c1,default=lambda obj:obj.__dict__)
# print(a)
#
# b=json.loads(a)
# print(b)