#Tip Calculator

print("Welcome to Tip Calculator.\n Hope you enjoyed your MEAL")
print()
check = float(input("What was/is your Total Bill?: "))
print()
tip = float(input('At how much percentage would you like to tip?: '))
print()
split_bill = int(input("How many peolpe to spill the bill among?: "))

pay =(((check*tip/100)) / split_bill)

print(f'Each indivisual shall pay R{pay}')