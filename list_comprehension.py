import copy

number = [1,2,3,4,5,6,7,8]


res = [(val ** 2) for val in number]
print(number)
print(res)

print([val for val in number if val%2==0])

my_tuple = []
my_set = []
for x in range(5):
    for y in range(5):
        my_tuple.append((x,y))
        my_set.append({x,y})

print(my_tuple)
print(my_set)

num = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
num1 = [row[:] for row in num]
print(num1)
#num1 = copy.deepcopy(num)

# to make it one dimension

num2 = [val for row in num for val in row]
print(num2)

name =""

print([val for val in name])

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
filtered = [row[1] for row in matrix if row[1] % 2 == 0]
print(filtered)
print([row for row in matrix])
print([row[:] for row in matrix])