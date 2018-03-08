#wuyujie



class stack(object):

    def __int__(self):
        self.list=[]
        self.size=0
        pass
    @property
    def size(self):
        return self

    @size.getter
    def  size(self):
        return self.size

    def push(self,d):
        if not isinstance(d,int):
            raise ValueError("must be int value")
        self.list.append(d)
        self.size=self.size+1


    def pop(self):
        if self.size ==0:
            raise ArithmeticError("self.size == 0")
        return list.pop(self.size()-1)
    def __str__(self):
        return "stack 's size is %d" % self.size()


#
# st=map(lambda x:x+2,[32,34,546,45])
# for i in st:
#     print(i)


from collections import  Iterable


def swap(s):
    if len(s) <1:
        raise ValueError("str is empty")
    if not isinstance(s,Iterable):
         raise ValueError("s not support iterator")
    le=int(len(s)/2)

    for i in s:
         t=s[i]
         s[i]=s[len(s)-i-1]
         s[len(s) - i - 1]=t
    return s


#print(s.pop())


print(swap("123"))