def fun():
    #indexing =  [start:end:step] to access string elements

    """
        str[:]  all elements
        str[-1] last elements
        str[0:-1] from start to second last (exclude last elements)
        str[::2] increment by 2 step
        str[-4:] last four elements

    """

    #print(help(str)) #find str methods and more
    #print(dir(str))  #don't know yet

    var1 = "My name is Alvi"
    var2 = """This is multiline 
    sentence..."""
    #print(var1)
    #print("Alvi" in var1)
    #print(var1[3:7])
    #print(var2[4:10])
    #print(var1[-1]) #last character

    #print(var1.find("i")) #find character/Word(A,Alvi) from left side ->
    #print(var1.rfind("i")) #find from right side <-
    #print(var1.index("name"))
    #print(len(var1))

    print(var1.count(" "))  #count space to anything
    print(var1.replace(" ","_  "))

    print(var1.isdigit()) #return true if string has only digit
    #print(var1[:])
    #print(var1[-1])
    print(var1[::2])




    for i in "banana":
        #print(i)
        pass

    #print(var1*3)#same string in 3 times
    #print(var1.upper())
    #print(var1.lower())







    #Encoding <-> Decoding
    str1 = "hello world"
    print(str1)
    str_encode=str1.encode("utf_16","strict") #utf_32
    print(str_encode)
    str_decode=str_encode.decode("utf_16","strict")
    print(str_decode)

if __name__ == '__main__':
    fun()