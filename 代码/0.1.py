sum = 0 
l = input("请输入5个数")
m = l.split(',')
for x in m:
    a = int(x)
    if a < 0:
        break
    sum += a
print("平均数为%f"%(sum/5))




