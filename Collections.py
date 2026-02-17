"""
 list = []  #Ordered      #duplicate value        #mutable (Changeable)
 tuple = () #Ordered      #duplicate value        #immutable (Not changeable)
 set = {}   #Not_ordered  #no duplicate value     #mutable (changeable)
 dict = {}  #Ordered      #no duplicate key:value #mutable(changeable)

 mutable = can be modified after create
 immutable = can't be modified after create

"""



"""
        ----- List ------
"""

list1 = ["Alvi",22,3.4,True]
#print(list1.index(22))
#print(list1.count("True"))  #I don't know yet this method
#print(type(list1))
fruits = ["Apple","Banana","Orange","Pineapple","Mango","Orange"]
#print(fruits[::2]) #print by 2 (step)
# new_fruits = [i for i in fruits]
# print(new_fruits)
for fruit in fruits:
    #print(fruit)
    pass

#print("Apple" in fruits) #bool
#print("Coconut" not in fruits)
#print(*fruits) #remove 3rd bracket
fruits[0]="Coconut" #override
#print(fruits)
fruits.insert(0,"Cherry")
fruits.append("Cherry") #add value at the end of list
fruits.remove("Cherry")
fruits.pop(0)
#print(fruits)
fruits.sort()
fruits.clear() #empty the list

#print(dir(list1))  #dont't know much
#print(help(list1)) #don't know much


"""
        ----- Tuple ------
"""
tuple1 = ("Apple","Banana","Orange")
#tuple1[0]="Cherry" #immutable can't do any change after create
#print(tuple1)
tuple2 = ("Coconut","Lime")
print(tuple1.__add__(tuple2))





"""
        ----- Set ------
"""

set1 = {"Apple","Banana","Orange"}   #unordered #ignore duplicate value
set1.add("Cherry")    #though immutable but can add/ remove
#set1.remove("Cherry")
set1.pop() #removes any item
#print(set1)




"""
        Set   <->  Tuple  <->   List  Conversion 
"""

list2 = list(set1)
tuple2 = tuple(list2)
set2 = set(tuple2)
print(f"{type(list2)}: {list2}")  #f means formated string
print(f"{type(set2)}: {set2}")
print(f"{type(tuple2)}: {tuple2}")

"""
        ----- Dictionary ------
"""

dict1 = {"Name":"Alvi","Age":22,"Dept":"CSE","City":"Dhaka"}
print(dict1)
print(type(dict1))
print(dict1.keys())
print(type(dict1.keys()))
print(dict1.items())
print(dict1.fromkeys("Name","12"))  #I don't know about this method use case yet...
print(dict1.get("Dept"))
dict1.update({"Country":"Bangladesh"})
print(dict1)
print(dict1.pop("Country"))
print(dict1)


#To iterate over all the key
for key in dict1.keys():
    print(f"{key} ",end=" ")
print()
#To iterate over all the values
for value in dict1.items():
    print(f"{value} ", end=" ")
print()
#or only values
for value in dict1.values():
    print(f"{value} ",end=" ")

for key, value in dict1.items():
        print(f"{key} = {value}",end=" ")

print()
"""
    More practice 
    list comprehension =[expression for value in iterable condition]
"""

#sepereatre positive and negative
numbers = [1,4,-9,8,5,-2,7,-6]
#list comprehension
positive = [x for x in numbers if x>=0]
negative = [y for y in numbers if y<0]
print(positive)
print(negative)



fruits1 = ["Apple","Mango","Banana","Kiwi"]
for i in fruits1:
    print(f"{i}",end=" ")



print()
fruits2 = ("Cherry","Coconut","Orange")
for i in fruits2:
    print(f"{i}", end=" ")

print()
fruits3 = {"Mango","Cherry","Lemon","Lime","Apple","Mango"}
for i in fruits3:
    print(f"{i}", end=" ")

print()
fruits4 = {"sweet":["Apple","Banana","Mango"],
          "sour":["lemon","lime","kiwi"],
          "bitter":"grape"}
print(fruits4.get("sweet"))

#print all (key,value)
for i in fruits4.items():
        print(i)


for i in fruits4.keys():
        print(i)

for i in fruits4.values():
        print(i)
