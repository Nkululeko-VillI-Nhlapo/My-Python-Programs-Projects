#Name: Nhlapo Nkululeko
#StuNum: 4129962
#Question 2

#Breaks down the amount entered into seperate notes
amount = float(input("Please enter the amount e.g. 456.32 for R456.32: R"))
r200 =amount // 200
remaining = amount % 200
amount = remaining
r100 = amount // 100
remaining = amount % 100
amount = remaining
r50 = amount // 50
remaining = amount % 50
amount = remaining
r20 = amount // 20
remaining = amount % 20
amount = remaining
r5 = amount // 5
remaining = amount % 5
amount = remaining
r2 = amount // 2
remaining = amount % 2
amount = remaining
r1 = amount // 1
remaining = amount % 1
print("Here’s the breakdown:")
print("R200: " + str(r200))
print("R100: " + str(r100))
print("R50: " + str(r50))
print("R20: " + str(r20))
print("R5: " + str(r5))
print("R2: " + str(r2))
print("R1: " + str(r1))
print("Here’s what’s remaining: R" + str(remaining))