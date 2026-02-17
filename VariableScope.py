"""
 variable scope = Where variable can be seen and accessible
 flow of scope (LEGB) =Local -> Enclosed -> Global -> Build in
"""

import math

def fun1():
    x = 1 #local variable
    print(x)
def fun2():
    x = 2 #local variable
    print(x)

def fun3():
    x = 3
    def fun4():
        print(x) #x is now enclosed variable
    fun4()
def fun5():
    print(y)

y = 5 #Global variable
fun1()
fun2()
fun3()
fun5()
print(math.pi) #pi built in variable