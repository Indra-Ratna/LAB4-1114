#Indra Ratna
#CS-UY 1114
#28 September 2018
#Lab 4
#Problem 7
item_1 = float(input("Enter price of first item: "))
item_2 = float(input("Enter price of second item: "))
cc = input("Does customer have aclub card?(Y/N):")
tax = float(input("Enter tax rate, e.g. 5.5 for 5.5% "))
base = item_1 + item_2
print("Base price: ",base)
if(item_1>=item_2):
    item_2 *=(1/2)
    discount = item_2+item_1
else:
    item_1 *=(1/2)
    discount = item_1+item_2
print("Price after discounts: ",discount)
if(cc == "Y"):
    cc_dis = discount*0.9
    print("Price after club card discount: ",cc_dis)
    total = (discount*(1+(tax/100)))*0.9
else:
    total = (discount*(1+(tax/100)))
print("Total price: ",format(total,".2f"))
