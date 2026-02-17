def start_code():
    str1='Count vowel from this statement'
    str2="aeiou"
    count=0
    for i in str1:
        if i.lower() in str2:
            count+=1
    print(count)

    list1=["A",12,5.5,True]
    print(list1)
    list1[3]=15
    print(list1)

if __name__ == "__main__":
    start_code()