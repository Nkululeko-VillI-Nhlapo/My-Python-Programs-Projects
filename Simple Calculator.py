#Nhlapo Nkululeko Villicent
#4129962
#The simple calculator program.

print("Hello, Welcome to the Simplest Calculating Program \n We +-/ and * Numbers For You")
print()

def ADD(num1,num2):
    output = num1 + num2
    operation = 'Adding'
    result(operation,num1,num2,output)

def SUBT(num1,num2):
    output= num1 - num2
    operation = 'Subtracting'
    result(operation, num1, num2, output)

def MULT(num1,num2):
    output = num1 * num2
    operation = 'Multiplying'
    result(operation, num1, num2, output)

def DEVI(num1,num2):
    dev = num1 / num2
    operation = 'Dividing'
    result(operation, num1, num2, dev)

def result(operation,num1,num2,output):
    print('The result of {0} {1} and {2} is {3}'.format(operation,num1,num2,output))


while True:

    C = input(
        "To continue Select, A to Add, S to Subtract, M to Multiply or D to Divide, the two numbers \n  To Quit the Program, Please Press Q: ")

    if C.upper() == 'Q':
        print("Thank You, for trying out this Very Simple Calculator")
        break

    print()
    A = int(input("Enter first Number: "))
    print()
    B = int(input("Enter second Number: "))

    if C.upper() == 'S':
            SUBT(A, B)

    elif C.upper() == 'A':
        ADD(A,B)
    elif C.upper() == 'M':
         MULT(A, B)
    elif C.upper() == 'D':
         DEVI(A, B)
    else:
        print("INVALID, Try Again")



















