#wuyjie


def isold(x):
    if x&1 == 0:
        return x



def greatthen10(x):
    if x > 4:
        return x



m=filter(isold,[1,2,3,4,5,6])

for i in m:
    print(i)

n=filter(greatthen10,[1,2,3,4,5,6])

for i in n:
    print(i)