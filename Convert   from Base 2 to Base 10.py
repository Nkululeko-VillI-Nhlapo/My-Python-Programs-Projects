def convertor(number, toBase):
  rem = []

  while True:
    w = number // toBase
    r = number % toBase
    rem.append(w)
    number = r
    if number <= 0 :
      break

  return

numInBase2 = int(input("Please enter a number in base 2: "))
numToBeConverted = 2

answer = convertor(numInBase2, numToBeConverted)

print(answer)