#

def engine (number, toBase):
    rem = []
    while True:

        w = number // toBase
        r = number % toBase
        rem.append(r)
        number = w
        if number <= 0:
             break
    remRev = rem[::-1]
    return remRev

print("Welcome to our Base COnvertor")

Num2BeConverted = int(input("Please Enter a number in base 10 to be convereted to a different base: "))
base = int(input('Enter base: '))

answer = engine(Num2BeConverted, base)
print(answer)


