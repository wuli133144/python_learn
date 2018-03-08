from collections import    Iterable


print(isinstance("asdfasdf",Iterable))


"""遍历一个lsit"""


from functools import  reduce


def convert(x,y):
    return x*10+y


def char2int(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

"""str2int"""
def str2int(s):
    return reduce(convert,map(char2int,"122324343"))



print(reduce(convert,map(char2int,"122324343")))


for i in "1234234124":
    print(i)



from collections import  Iterable

print(isinstance("41234214",Iterable))




print("++++++++++++++++char2int+++++++++++")
print(char2int('3'))
print("+++++++++++++++char2int end++++++++")

List=[12,234,345,56,5,67][:3]


dictor={"name":"wuyujie","age":23}["age"]
print(dictor)

print(List)

print(List)

for i in List:
    print(i)

"""enumerate iterator value

"""

for index,value in enumerate(List):
    print("List[{i}]={va}".format(i=index,va=value))




