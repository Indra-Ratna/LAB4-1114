#Indra Ratna
#CS-UY 1114
#28 September 2018
#Lab 4
#Problem 6
f_24 = int(input("Please enter time in 24 hr format :"))
hours = f_24//100
minutes = f_24%100

hours_12 = ""
minutes_12 = ""
ap = ""
if(hours == 0):
    hours_12 = str(12)
    ap = "am"
elif(hours == 12):
    hours_12 = str(12)
    ap = "pm"
elif(1<=hours<10):
    hours_12 = str(hours).zfill(2)
    hours = hours_12
    ap = "am"
elif(10<=hours<=11):
    hours_12 = str(hours)
    ap = "am"
elif(hours>12):
    hours_12 =str(hours-12)
    ap = "pm"


if(minutes<10):
    minutes_12= str(minutes).zfill(2)
    minutes = minutes_12
else:
    minutes_12 = str(minutes)

print(str(hours)+":"+ minutes+" in 12 hour format is "+hours_12+":"+minutes_12+" "+ap)
