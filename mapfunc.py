#wuyujie


"""
wuyujie
doc
"""

def add(x):
    return x*x


def less10(x):
    if x > 10:
        return x
    elif x<10:
        return x+1

l=map(add,[12,34,345])


m=filter(less10,[1,2,3,4,5])

for i in m:
    print(i)


for i in m:
    print(i)


for i,value in enumerate(l):
    print(i,value)



class obj(object):
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    """__str__"""
    def __str__(self):
        print("username{name}".format(name=self.__name))

    """setname()"""
    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name

    def setage(self,age):
        self.__age=age
    def getage(self):
        return self.__age



class animal(object):

    __slots__ = ("name") #__slots__代表可以使用的属性值，超出这个范围就不可以使用了

    def __init__(self,name,age=12):
        self.name=name
        self.age=age

    def getname(self):
        return self.name
    def setname(self,name):
        self.name=name
    def run(self):
        print("running .......")
    def __str__(self):
        return "name is"+self.name




class dog(animal):
    def run(self):
        print("dog is running......")
    def __str__(self):
        return "dog's name"+self.name



class student(object):
    """fasdkljs"""
    __slots__ = ("name","age","score")
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def set_score(self,s):
        if not isinstance(s,int) :
            raise ValueError("s must be int")
        elif s < 0 or s >100 :
            raise ValueError("s must great 0")

    @property
    def score(self):
        return self.score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise  ValueError("value must be int")
        elif value <0 or value >100:
            raise ValueError("value must be int")
        self.score=value

    @score.getter
    def score(self):
        return self.score

    def __str__(self):
        return "student's name is %s" % self.name #ok


    def __getitem__(self, n):
        return "xxxxx"

    def __iter__(self):
        return self
    def __next__(self):
        return "xxx"
    def __call__(self, *args, **kwargs):
        print("xxxxxxxxcall")





#史记，资质通鉴

s=student("wuyjie",23)
s()
print(s)
print(s[2])







#
# a=animal("fdsafasdf animal")
#
# print(a.name)
# print(a.age)
#
# d=dog("fdsafs")
#
# d.run()

#print(str(dog))


"""
main=obj("wuyuhjie",23)
print(type(main))
print(dir(main))
print(isinstance(main,obj))#isinstance

print(main._obj__age) #可以直接访问的结构

print(main._obj__name)#可以直接访问name

print(main.getage())

"""