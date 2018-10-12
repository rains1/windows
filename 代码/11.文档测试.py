'''
文档测试：
1.导入doctest模块
'''
import doctest

def mySum(x,y):
    '''
    求x和y的和
    :param x:第一个
    :param y:第二个
    :return:2数之和
    example:
    >>> print(mySum(1,2))
    3
    '''
    return x+y+1

doctest.testmod()