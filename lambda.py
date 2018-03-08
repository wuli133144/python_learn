#wuyujie



""""lambda test"""



def add(x):
    return x+1

#列表表达式不常用，但是方便

print([i for i in map(add,[12,23,34])])

res=map(lambda x:x+1,[12,3,4,5])


#good

"""lambda表达式是比较好用的
    列表表达式也是可以使用的表达式
"""






print([i for i in map(lambda x:x+1,[12,34,45])])



for i,value in enumerate(res):

    print(value)



    """
     现在测试一下 dict数据结构
    
    """
print("=======================dict============")

dictor={"name":"wuyujie","age":23}
print(dictor)

for i ,value in dictor.items():
    print(i,value)







