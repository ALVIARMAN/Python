# 0,1,1,2,3,5,8,13,21

#GLOBAL VARIABLE
count = 2

def fib(n):
    first = 0
    second = 1
    print(f"{first}, {second}, ",end="")
    while n!=0:
        next_num = first + second
        print(f"{next_num}, ",end="")
        first = second
        second = next_num
        n-=1



#recursive function
def recur(first,second):
    global count #access global variable
    if count > 19:
        return
    else:
        next_num = first + second
        print(f"{next_num}, ",end="")
        first = second
        second = next_num
        count +=1
        recur(first,second)


def nth_fib(n):
    if n <= 1:
        return n
    else:
        return nth_fib(n-1)+nth_fib(n-2)

if __name__ == "__main__":
    fib(18)
    print()
    print(f"0, 1, ",end='')
    recur(0,1)
    print()
    print(nth_fib(5))