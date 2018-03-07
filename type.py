#wuyujie
#type


sets=["wuyuuie","fasdfasd","fasdfas","jackwu"]

print(sets[1:-1])


#sets 去除下标sets[1]----sets[3](注意不包括3)

print(sets[1:3])
print(sets[1:4])

for i in sets:
     print(i)

print("===========================append======================")
"""追加数据"""
sets.append("xxxxxx")
sets.append("xxxxxx")
sets.append("xxxxxx")
sets.append("xxxxxx")
sets.append("xxxxxx")

for i in sets:
     print(sets)
"""删除数据"""

print("===========================delete======================")

del  sets[-1]
del  sets[-2]
del  sets[-3]

for i in sets:
     print(sets)

print("=========================modify========================")

sets[-1]="sets[-1]"
sets[-2]="sets[-2]"
sets[-3]="sets[-3]"

for i in sets:
     print(sets)


print("============================insert======================")

sets.insert(2,"jackuw")
sets.insert(3,"jackuw1")
sets.insert(4,"jackuw2")
sets.insert(5,"jackuw3")
for i in sets:
     print(sets)


print("===========================三元运算======================")

a,b,c=12,23,345

d= a if a> c else b #good
print(d)

#if __name__ == '__main__':




if __name__ == '__main__':
     print(type("xxxxxx"))
     print(type(12233))
     print(type(True))
     print(type(bool))

