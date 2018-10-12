import  time

#获取当前时间的时间戳
# 从1970年1月1日0点开始到现在的时间差的毫秒值
c1=time.time()
print("时间戳：%f"%c1)

#将时间戳转为元组（世界标准时间）
c2=time.gmtime(c1)
print(c2)

#将时间戳转为本地时间,结果存储在元组中
c3=time.localtime(c1)
print(c3)
#将时间元组转为时间戳
print(time.mktime(c2))
#将时间元组转为字符串Sat Jun 23 16:25:27 2018
str1=time.asctime(c3)
print(str1)
#将时间戳转为字符串Sat Jun 23 16:25:27 2018
str2=time.ctime(c1)
print(str2)
#format 将时间转换成指定格式的字符串
str3=time.strftime("%Y年%m:%d %H:%M:%S")
print(str3)
#将指定格式的字符串转换为时间元组
tuple1=time.strptime(str3,"%Y年%m:%d %H:%M:%S")
print(tuple1)
#获取程序执行时间
# print(time.clock())
# sum=0
# for i in range(100000000):
#     sum+=i
# print(time.clock())

#程序休眠时间
# time.sleep(3)
# print("over")


#导入日历模块
import calendar
#获取指定月份的日历
print(calendar.month(2018,6))
#获取指定年份的日历
print(calendar.calendar(2018))
#判断是否是闰年
print(calendar.isleap(2018))
#获取指定的月份有多少天和这个月的第一天锁对应的星期
#星期一代表0一次递增
print(calendar.monthrange(2018,8))


