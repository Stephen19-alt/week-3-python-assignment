print("Hello Children!")

a= 5
b= 10
a * b
print(a * b)
str_counter = 0
for item in ("Stephen", "Sabbath", 10, 12, "Anyango"):
    if isinstance (item, str):
        str_counter += 1

print(str_counter)

Length = 10
Width = 14
Height = 9
Volume = Length * Width * Height
print (Volume)
int_counter = 0
for item in (10.5, 5, 6, "Stephen", "Machakos", 18):
    if isinstance (item, int):
        int_counter += 1
print (int_counter)
float_counter = 0
for item in (10.8, 15.9, "Stephen", "Daniel", 12.3, 19.0):
    if isinstance (item, float):
        float_counter += 1
print (float_counter)
float_counter

a= 10
if a > 5:
    print ("a is greater than 5")
else:
    print ("a is less than 5")

c = 15
if c < 20:
    print ( "c is less than 20")
else:
    print ("c is greater than 20")

#prompt the user to enter marks
marks = int(input("Enter the student marks(0-100): "))
# grading system based on marks
if marks > 70:
    print ("Excellent")
elif marks >= 60:
    print ("Very Good")
elif marks >= 50:
    print ("Good")
elif marks >= 40:
    print ("Fair")
elif marks >= 30:
    print ("Poor")
else:
    print ("Very Poor")



# University Grading Model
# prompt user to input marks the grade category
points = int(input("Please supply the points(0-100): "))
# Grade category based on points
if points > 70:
    print ("First Class Honours")
elif points >= 60:
    print ("Second Class Honours (Upper Division)")
elif points >= 50:
    print ("Second Class (Lower Division)")
elif points >= 40:
    print ("Pass")
else:
    print ("Fail")

    










