#program let user enter  a base price of a car
#adds additional fees
# prints actual price of a car


#prompt the user for base price
base_price=int(input("please enter the base price price of this car "))
#assign tax
tax=(base_price * 2)/100
#assign license
licence=(base_price * 3)/100
#assign dealer prep
dealer_prep= 50
#assign destination charge
destination_charge=30
actual_price=base_price+tax+licence+dealer_prep+destination_charge
print("the actual price of this car is","$",actual_price)

