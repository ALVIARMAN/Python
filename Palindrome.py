#121 <-> 121 same in reverse order

def fun(number):
    temp=number
    result=remain=0
    while temp!= 0:
        remain=temp%10
        result=result*10+remain
        temp//=10

    #conditional statements(Ternary Operator)
    check = "Palindrome" if result == number else "Not Palindrome"
    print(check)




if __name__ == '__main__':
    fun(int(input("Enter a number: ")))