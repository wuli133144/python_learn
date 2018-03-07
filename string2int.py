

#wuyujie

# string2 int


def string2int1(s) :
    return eval(s)


#def string2int2(s):
#    return int(s)


def convert(x,y):
    return x*10+y

def char2int(s):
    arr={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]




from functools import  reduce

def string2int(s):
      return reduce(convert,map(char2int,s))

if __name__ == '__main__':

    """test string2int2"""

    str=input("string:")
    num=string2int1(str)
    print(num)
    print(type (num))


    print("string to int")
    num1=string2int(str)
    print(num1)
    print(type(num1))
