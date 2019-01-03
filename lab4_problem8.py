#Indra Ratna
#CS-UY 1114
#28 September 2018
#Lab 4
#Problem 8
shape = ""
sides =int(input("Enter the number of sides :"))


if(sides == 3):
    shape = "triangle"
    equals = int(input("How many sides are of equal length ?:"))
    if(equals==3):
             print("The shape is an equilateral triangle")
    elif(equals ==2):
        degree = int(input("What is the degree of the largest angle of the triangle ?"))
        if(degree >90):
            print("The shape is an isosceles obtuse triangle")
        elif(degree==90):
            print("The shape is an isosceles right triangle")
        elif(degree<90):
            print("The shape is an isosceles acute triangle")
elif(sides ==4):
    shape = "square"
    opp_equal = input("Are the opposite sides of equal length ? ( Y / N ):")
    if(opp_equal =="N"):
        print("The shape is a quadrilateral")
    elif(opp_equal =="Y"):
        degrees = input("Are the angles 90 degrees ?:")
        if(degrees == "N"):
            print("The shape is a paralellogram")
        elif(degrees == "Y"):
            equal = input("Are all the sides of equal length?(Y/N):")
            if(equal =="Y"):
                print("The shape is a square")
            elif(equal == "N"):
                print("The shape is a rectangle")
            
