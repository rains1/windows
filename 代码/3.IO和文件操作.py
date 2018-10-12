'''
StringIO:存数据，存储在内存中
'''

from io import StringIO

s=StringIO()
s.write("20")
s.write("hh")
s.write("aa\nbb")
s.seek(5)
a=s.readline()
print(a)
# print(s.getvalue())

f=open(r"/Users/yang/Desktop/111副本.txt","a+")
f.write(s.getvalue())
f.close()

from  io import BytesIO

by=BytesIO()
by.write("你好".encode())
print(by.getvalue().decode())
