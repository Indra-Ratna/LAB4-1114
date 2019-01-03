#Indra Ratna
#CS-UY 1114
#28 September 2018
#Lab 4
#Problem 6
f_24 = int(input("Please enter time in 24 hr format :"))
hours_o = f_24//100
hours = 0
minutes = f_24%100
a_or_p = ""

if(hours_o>12):
    a_or_p= "pm"
    if(hours<10):
        hours=str(hours).zfill(2)
elif(hours_o==12):
    a_or_p = "pm"
elif(hours_o ==0):
    hours = 12
    a_or_p = "am"
else:
    a_or_p ="am"
    if(hours<10):
        hours=str(hours_o).zfill(2)

minutes_n = ""    
if(minutes<10):
    minutes_n = str(minutes).zfill(2)
else:
    minutues_n = str(minutes)
print(str(hours_o)+":"+str(minutes)+" in 12 hour format is "+str(hours)+":"+minutes_n+" "+a_or_p)
