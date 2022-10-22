def con2(b):
  digits = []
  a = int(input("Enter the 1st digit: "))
  b = int(input("Enter the 2nd digit: "))


  digits.append(a)
  digits.append(b)


  calculations1 = digits[0]*pow(2,len(digits)-1)
  calculations2 = digits[1]*pow(2,len(digits)-2)


  sum = calculations1 + calculations2
  print(f'Your answer in Base 10 is {sum}')
def con3(b):
  digits = []
  a = int(input("Enter the 1st digit: "))
  b = int(input("Enter the 2nd digit: "))
  c = int(input("Enter the 3rd digit: "))

  digits.append(a)
  digits.append(b)
  digits.append(c)

  calculations1 = digits[0]*pow(2,len(digits)-1)
  calculations2 = digits[1]*pow(2,len(digits)-2)
  calculations3 = digits[2]*pow(2,len(digits)-3)

  sum = calculations1 + calculations2 + calculations3

  print(f'Your answer in Base 10 is {sum}')
def con4(b):
  digits = []
  a = int(input("Enter the 1st digit: "))
  b = int(input("Enter the 2nd digit: "))
  c = int(input("Enter the 3rd digit: "))
  d = int(input("Enter the 4th digit: "))

  digits.append(a)
  digits.append(b)
  digits.append(c)
  digits.append(d)

  calculations1 = digits[0]*pow(2,len(digits)-1)
  calculations2 = digits[1]*pow(2,len(digits)-2)
  calculations3 = digits[2]*pow(2,len(digits)-3)
  calculations4 = digits[3]*pow(2,len(digits)-4)

  sum = calculations1 + calculations2 + calculations3 + calculations4

  print(f'Your answer in Base 10 is {sum}')

def con5(b):
  digits = []
  a = int(input("Enter the 1st digit: "))
  b = int(input("Enter the 2nd digit: "))
  c = int(input("Enter the 3rd digit: "))
  d = int(input("Enter the 4th digit: "))
  e = int(input("Enter the 5th digit: "))

  digits.append(a)
  digits.append(b)
  digits.append(c)
  digits.append(d)
  digits.append(e)

  cal1 = digits[0]*pow(2,len(digits)-1)
  cal2 = digits[1]*pow(2,len(digits)-2)
  cal3 = digits[2]*pow(2,len(digits)-3)
  cal4 = digits[3]*pow(2,len(digits)-4)
  cal5 = digits[4]*pow(2,len(digits)-5)

  sum = cal1 + cal2 + cal3 + cal4 + cal5

  print(f'Your answer in Base 10 is {sum}')

def con6(b):
  digits = []
  a = int(input("Enter the 1st digit: "))
  b = int(input("Enter the 2nd digit: "))
  c = int(input("Enter the 3rd digit: "))
  d = int(input("Enter the 4th digit: "))
  e = int(input("Enter the 5th digit: "))
  f = int(input("Enter the 6th digit: "))

  digits.append(a)
  digits.append(b)
  digits.append(c)
  digits.append(d)
  digits.append(e)
  digits.append(f)

  cal1 = digits[0]*pow(2,len(digits)-1)
  cal2 = digits[1]*pow(2,len(digits)-2)
  cal3 = digits[2]*pow(2,len(digits)-3)
  cal4 = digits[3]*pow(2,len(digits)-4)
  cal5 = digits[4]*pow(2,len(digits)-5)
  cal6 = digits[5]*pow(2,len(digits)-6)

  sum = cal1 + cal2 + cal3 + cal4 + cal5 + cal6

  print(f'Your answer in Base 10 is {sum}')
def con7(b):
  digits = []
  a = int(input("Enter the 1st digit: "))
  b = int(input("Enter the 2nd digit: "))
  c = int(input("Enter the 3rd digit: "))
  d = int(input("Enter the 4th digit: "))
  e = int(input("Enter the 5th digit: "))
  f = int(input("Enter the 6th digit: "))
  g = int(input("Enter the 7th digit: "))

  digits.append(a)
  digits.append(b)
  digits.append(c)
  digits.append(d)
  digits.append(e)
  digits.append(f)
  digits.append(g)

  cal1 = digits[0]*pow(2,len(digits)-1)
  cal2 = digits[1]*pow(2,len(digits)-2)
  cal3 = digits[2]*pow(2,len(digits)-3)
  cal4 = digits[3]*pow(2,len(digits)-4)
  cal5 = digits[4]*pow(2,len(digits)-5)
  cal6 = digits[5]*pow(2,len(digits)-6)
  cal7 = digits[6]*pow(2,len(digits)-7)

  sum = cal1 + cal2 + cal3 + cal4 + cal5 + cal6 + cal7

  print(f'Your answer in Base 10 is {sum}')
def con8(b):
  digits = []
  a = int(input("Enter the 1st digit: "))
  b = int(input("Enter the 2nd digit: "))
  c = int(input("Enter the 3rd digit: "))
  d = int(input("Enter the 4th digit: "))
  e = int(input("Enter the 5th digit: "))
  f = int(input("Enter the 6th digit: "))
  g = int(input("Enter the 7th digit: "))
  h = int(input("Enter the 8th digit: "))


  digits.append(a)
  digits.append(b)
  digits.append(c)
  digits.append(d)
  digits.append(e)
  digits.append(f)
  digits.append(g)
  digits.append(h)


  cal1 = digits[0]*pow(2,len(digits)-1)
  cal2 = digits[1]*pow(2,len(digits)-2)
  cal3 = digits[2]*pow(2,len(digits)-3)
  cal4 = digits[3]*pow(2,len(digits)-4)
  cal5 = digits[4]*pow(2,len(digits)-5)
  cal6 = digits[5]*pow(2,len(digits)-6)
  cal7 = digits[6]*pow(2,len(digits)-7)
  cal8 = digits[7]*pow(2,len(digits)-8)

  sum = cal1 + cal2 + cal3 + cal4 + cal5 + cal6 + cal7 + cal8

  print(f'Your answer in Base 10 is {sum}')

print("Welocome.The program helps you convert numbers from base2 to base 10")
length = int(input("How many are your digits in base 2, e.g 1,0,1,1 = 4: "))
if (length == 2):
  con2(length)
elif(length == 3):
  con3(length)
elif(length == 4):
  con4(length)
elif(length == 5):
  con5(length)
elif(length == 6):
  con6(length)
elif(length == 7):
  con7(length)
elif(length == 8):
  con8(length)
else:print('bye')