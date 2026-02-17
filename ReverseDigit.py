def fun(number):
    result = 0
    remain = 0
    while number > 0: #number != 0
        remain = number % 10
        result = result * 10 + remain
        number //= 10
    print(result)


if __name__ == "__main__":
    fun(int(input("enter a number: ")))