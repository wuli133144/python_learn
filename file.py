


#wuyujie




import  sys
import  os


def filecheck():
    bres=os.path.exists("checklog.log")
    info=[]

    if bres :
        with open("checklog.log","r") as f:

           content=f.readline()
           print(content)
           len=len(content)
           #print(len)
           if(len <1):
               os._exit(1)

           arr=content.split(',')
           for i, value in enumerate(arr):
               if i==3:
                   info.append(value)
               elif i ==8:
                   info.append(value)

           for i in info:
               print(i)



def filelog():
    info=[]
    bres=os.path.exists("checklog.log")
    if bres :
        with open("checklog.log","r") as f:
            contents=f.readlines()
            for i in contents:
                 arr=i.split(',')
                 info.append(arr[2])
                 info.append(arr[8])



    print(info)



if __name__ == '__main__':
    #filelog()

    dir=os.path.dirname(".")
    dirname=os.listdir(".")
    #print(dirname)
    for i in dirname:
        if os.path.isfile(i):
            #print("{file} is file".format(file=i))
            if i.endswith(".py"):
                print("{i} is python file".format(i=i))


    #print(dir)
    print(os.path)