#创建字符串
str1="hello"
str2="world "
#2个字符串做加法操作 拼接操作
str3=str1+str2
print(str3)
#字符串做乘法  重复输出几次
print(str3*2)

#下标（索引 index）
print(str1[4])
#获取字符串的长度
str4="abcd"
print(len(str4))
#判断某个单词在不在字符串内
print("ac" in  str4)

str5="abCd"
#大写转小写
print(str5.lower())
#小写转大写
print(str5.upper())
#大转小 小转大
print(str5.swapcase())
#将首字母转大写，其余小写
print(str5.capitalize())
str6="hello world abc"
#将每个单词的首字母大写
print(str6.title())

str7="helloll"
#检测字符串中某个单词出现的次数
print(str7.count("ll"))

str8="helo wlorld"
print(str8.rfind("l"))
print(str8.find("0",3,7))
# print(str8.index("0"))

str9="hello world hello aa  hello"
print(str9[2:5])
print(str9[2:])
print(str9[:4])
print(str9.replace("hello","你好",2))
str10="hello"
print(str10.startswith("l"))
print(str10.endswith("o"))
print(str10.center(40,"*"))
print(str10.ljust(40,"*"))
print(str10.rjust(40,"*"))
print(str10.zfill(40))
print(str10.lstrip("h"))

str11="hello world"
print(str11.split("w"))
str12="hello\nworld\naaa"
print(str12.splitlines())
list1=["1","2","3"]
str13="-".join(list1)
print(str13)

#"10,20,30,40,50"
score=input("请输入成绩")
list2=score.split(",")
num=0
sum1=0
while num<5:
    a=int(list2[num])
    sum1+=a
    num+=1
print(sum1/5)