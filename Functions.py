# Creating Functions
from tkinter.font import names


def DATA():
    Data = {}

    no = int(input("Enter Number Of Subjects: "))

    x = 1

    while x <= no:
        subject = input("Enter Subject Name: ")
        marks = input("Enter Marks: ")

        Data[subject] = marks
        x += 1

    for sub, mark in Data.items():
        print(sub, mark)

# Default Parameters
def get_grade(marks = int() , subject='None'):


    if marks > 100 or marks < 0:
        print("Invalid Marks")
    elif marks >= 75:
        print( subject , ": A")
    elif marks >= 65:
        print(subject ,": B")
    elif marks >= 55:
        print(subject , ": C")
    elif marks >= 35:
        print(subject,": S")
    else:
        print(subject,": W")

# packed arguments using star mark in parameters
def sum(*marks):
    total = 0
    for i in marks:
        total += i
    print(total)
    print(type(marks))

sum(110,50)

# keyword argument
def g_form(**keyword):
    if 'name' not in keyword:
        name = "Error !"
    else:
        name = "Hi " , keyword['name']

    if 'age' not in keyword:
        age = "Error !"
    else:
        age = ("Your age is " , keyword['age'])

    if 'city' not in keyword:
        city = "Error !"
    else:
        city = "You are in " , keyword['city']

    print("Hansaka")

    return name , age , city


out1 = g_form(name = "Hansaka" , age = 19  ,   city="Maradankadawala")
out2 = g_form(name = "Vidushan" , city="Kekirawa")

print(out1 , "\n" ,out2)

for name,age in out1:
    print(name,age)
