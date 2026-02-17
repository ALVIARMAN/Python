def fun(num):
    result = 0
    count = 0
    while num !=0:
        result+=num%10
        num//=10
        count+=1

    print(f"Total digit is {count} and sum of digits is {result}")


if __name__ == "__main__":
    fun(125)



    '''
        125 Mod 10
        
            10|125|12
               10
               --
                25
                20
                --
            Right number ->  5 
        
    '''