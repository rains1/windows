'''
序列化：
'''
import pickle


# dic={"name":"张三",
#      "age":10}
# path=r"/Users/yang/Desktop/111副本.txt"
# f=open(path,"wb")
#
# # 对字典进行序列化
# dic_x=pickle.dump(dic,f)
# f.close()
#
# f1=open(path,"rb")
# abc=pickle.load(f1)
# print(abc)
# f1.close()

import json

class Cat:
      def __init__(self,name,age):
            self.name=name
            self.age=age

c1=Cat("aa",10)

path=r"/Users/yang/Desktop/111副本.txt"
f=open(path,"w")
# pickle.dump(c1,f)
json.dump(c1,f,default=lambda obj:obj.__dict__)
f.close()






