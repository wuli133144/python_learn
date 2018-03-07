#wuyujie
import  datetime
import  sys


if __name__ == '__main__':

      number=23
      while True:
          num=eval(input("input number:"))
          if num < 23:
              print("num={arg} is smaller".format(arg=num))
          elif num > 23:
              print("num={arg} is larger".format(arg=num))
          elif num == 23:

              print("right")
              break
