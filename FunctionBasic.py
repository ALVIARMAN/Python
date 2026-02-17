"""
  All about functions

  types of arguments :
   1.Positional 2.Default 3.Keyword 4.Arbitrary
"""

#common function with positional arguments
def addition(a,b):
    print(a+b)

#default parameter function
def summation(a,b=5):
    print(a+b)

#keyword arguments function
def division(a,b):
    result = a-b
    print(f"{result}")

#Arbitrary *args function
def total(*args):
    print(type(args))
    result = 0
    for i in args:
        result += i
    print(result)

#Arbitrary **kwargs arguments function
def multi(**kwargs):
    print(type(kwargs))
    result = 1
    for i in kwargs.values():
        print(f"{i}",end=" ")
        result *=i
    print(f" = {result}")

if __name__ == "__main__":
    addition(10,5)

    summation(10) #b has default value

    division(a=10,b=5) #keyword arguments

    total(5,10,15) #Arbitrary *args arguments
    total(20,10,5,15)

    multi(first=5,second=8) #Arbitrary **kwargs arguments
    multi(num1=15,num2=10,num3=15) #multiplication




"""
    Practice More
"""
def student_info(*args,**kwargs):
    for i in args:
        print(f"{i} ",end="")
    for i in kwargs.values():
        print(f"{i} ",end=" ")


student_info("Alvi",22,Dept="CSE",City="Dhaka")