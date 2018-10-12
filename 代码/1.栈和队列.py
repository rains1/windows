'''
栈：没有真正的栈，只能用list去模拟栈的存储
特点：先进后出
'''

# stack=[]
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack)
#
# print(stack.pop())
# print(stack)
# print(stack.pop())
# print(stack)
# print(stack.pop())
# print(stack)

'''
队列：先进先出
存数据：进队  取数据：出队
'''
from collections import deque

#创建一个空队列
qu=deque()
qu.append(10)
qu.append(20)
qu.append(30)
print(qu)
print(qu.popleft())
print(qu)