fruits = ["Apple", "Banana", "Cherry"]
meats =  ["fish", "turkey", "buffalo"]
vegetables = ["Cucumber", "Tomato", "Watermelon", "Potato"]
twoDlist = [fruits,meats,vegetables]
print(twoDlist)
#print(twoDlist[2].index("Potato"))
print(f"{len(twoDlist[0])}, {len(twoDlist[1])}, {len(twoDlist[2])}")

#get individual elements
#print(twoDlist[2][3]) #potato


# combine  one    two list
matrix = [[1,"Galib"] ,["Alvi",4], [5,"Masud"]]
#print(matrix[1]) #print second list

for i in matrix:
    for j in i:
        #print(j,end=" ") #eliminate newline statement at the end of the print
        pass
    #print()


"""
    [(),()] possible to create tuples inside a 2D list
    [{},{}] possible to create set inside a 2D list
    [{},()] possible to create set and tuple inside a 2D list
"""

list_tuple = [("Hi","Alvi"),("Hi","Masud")]
print(list_tuple)
print(type(list_tuple)) #list
print(type(list_tuple[1])) #tuple

list_set = [{"Apple","Banana","Orange"},{"Cucumber","Potato","Potato"}]
print(list_set)

list_tuple_set = [{"This" " is" " set"},("This"," is"," tuple")]
print(list_tuple_set)


"""
    Calculator Matrix
"""

keypad = [[7,8,9,"*"],
          [4,5,6,"/"],
          [1,2,3,"-"],
          [0,"+","c","="]
          ]

for row in keypad:
    for column in row:
        print(column,end=" ")
        pass
    print()

for i in keypad:
    print(i)

for i in range(len(keypad)):
    for j in range(len(keypad[i])):
        print(f"Row {i} Col {j} = {keypad[i][j]}")

