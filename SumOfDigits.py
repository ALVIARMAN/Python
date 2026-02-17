def fun(num):
    sum = 0
    while num > 0:
        sum = sum + num % 10
        num = num // 10
    return sum

if __name__ == "__main__":
    num = int(input("enter a number: "))
    num = fun(num)
    print(num)