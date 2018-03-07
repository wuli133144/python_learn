
#wuyujie
#
#


""" test map()
    arg:
    return:
"""

import  sys
import  math

from  functools import  reduce

def add(x):
    return x*x



""" map函数的使用
    第一个参数：函数名
    第二个参数：迭代序列[]
"""

l=map(add,[1,2,3,4,5])
for i in l:
    print(i)




def f(x,y):
    return x+y;


m=reduce(f,[1,2,3,4,5])

print("reduce result:")
print(m)









