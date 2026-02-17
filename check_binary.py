def func(n):
    if n == 0 or n == 1 or n < 0:
        return "Greater then 1 pls "
    while n!=0:
        if n % 10 > 1:
            return False
        n //= 10

    return True


if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print(func(n))