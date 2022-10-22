#Nhlapo Nkululeko Villicent
#4129962
#The simple calculator program(EXTEND)

print("Hello, Welcome to the Simplest Calculating Program \n We +,-,/,//,%,** and * Numbers For You")
print()

def ADD(num1,num2):
    sum = num1 + num2
    print('The Answer is = ',sum)

def SUBT(num1,num2):
    res = num1 - num2
    print('The Answer is = ',res)

def MULT(num1,num2):
    mul = num1 * num2
    print('The Answer is = ',mul)

def DEVI(num1,num2):
    dev = num1 / num2
    print('The Answer is = ',dev)

def EXPO(num1,num2):
    exp = (num1**num2)
    print('The Answer is = ', exp)
def MODU(num1, num2):
    mod = (num1%num2)
    print('The Answer is = ', mod)
def INTDEV(num1, num2):
    id = (num1 // num2)
    print('The Answer is = ', id)
def PERC(num1, num2):
    pec = (num1 / num2) * 100
    print('The Answer is = ', pec)
while True:

    choice = input(
        "To continue Select, A to Add\nS to Subtract\nM to Multiply\nD to Divide, \nE to Exponentiate \nMOD for Modullo Division \nI for Integer Division \nP for Percentage Calculation. \nTo Quit the Program, Please Press Q: ")

    if choice.upper() == 'Q':
        print("Thank You, for trying out this Very Simple Calculator")
        break

    print()
    first_num = int(input("Enter first Number: "))
    print()
    second_num = int(input("Enter second Number: "))

    if choice.upper() == 'S':
            SUBT(first_num, second_num)

    elif choice.upper() == 'A':
        ADD(first_num, second_num)
    elif choice.upper() == 'M':
         MULT(first_num, second_num)
    elif choice.upper() == 'D':
         DEVI(first_num, second_num)
    elif choice.upper() == 'E':
         EXPO(first_num, second_num)
    elif choice.upper() == 'MOD':
         MODU(first_num, second_num)
    elif choice.upper() == 'I':
         INTDEV(first_num, second_num)
    elif choice.upper() == 'P':
         PERC(first_num, second_num)

    else:
        print("INVALID, Try Again")

        print()