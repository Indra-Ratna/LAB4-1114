#Indra Ratna
#CS-UY 1114
#28 September 2018
#Lab 4
#problem 4
import turtle
x = input("Please enter 'R' for 'Right ’ or ’L ’ for ’ Left ’: ")
a = 120
d = 80

if(x=='R'):
    turtle.right(a)
    turtle.forward(d)
    turtle.right(a)
    turtle.forward(d)
    turtle.right(a)
    turtle.forward(d)
elif(x=='L'):
    turtle.left(a)
    turtle.forward(d)
    turtle.left(a)
    turtle.forward(d)
    turtle.left(a)
    turtle.forward(d)
else:
    print("Enter a valid response")
