#if and else statements
temperature = 29
if temperature>= 25:
    print("It is a hot day!")
else:
    print("It is a warm day")

# if elif statements
temp = 9
if temp > 22:
    print("It is a hot day!")
elif temp <= 22:
    print("It is a warm day!")
elif temp <= 15:
    print("It is a cool day!")
else:
    print("It is a very cold day!")

# for loop
box_of_fruits = ("orange", "cherry", "banana", "mango", "kiwi")
for fruit in box_of_fruits:
    print(fruit)

# while loop
count = 2
while count<= 5:
    print(count)
    count+=1

# Functions
def add(a, b):
    sum = (a+b)
    print(sum)
    add(20, 30)







