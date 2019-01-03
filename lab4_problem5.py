#Indra Ratna
#CS-UY 1114
#28 September 2018
#Lab 4
#Problem 5
import datetime
curr_year = int(datetime.datetime.now().strftime("%Y"))
name = input("Please enter the student’s name : ")
grad_year= int(input("Please enter the year that the student will graduate :"))
if(grad_year>curr_year):
    if(grad_year-curr_year==4):
        print(name+" is a Freshman")
    elif(grad_year-curr_year==3):
        print(name+" is a Sophmore")
    elif(grad_year-curr_year==2):
        print(name+" is a Junior")
    elif(grad_year-curr_year==1):
        print(name+" is a Senior")
    elif(grad_year-curr_year>4):
        print(name+ " is not yet in college")
else:
    print(name+" has graduated")
