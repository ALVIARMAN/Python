def fun(numbers):
    even=0
    odd=0
    for i in numbers:
        if i % 2 == 0:
            even += i
            print(f"This number is {i} even")
        else:
            print(f"This number is {i} odd")
            odd += i

    print(f"Sum of even number is {even}, Sum of odd number is {odd}")

if __name__ == '__main__':
    # list=[1,2,3,4,5,6]
    numbers=[3,4,5,6,7,8]
    fun(numbers)