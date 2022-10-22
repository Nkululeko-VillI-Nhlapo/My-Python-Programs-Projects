#Fibonacci Sequance
#From my own notice this is the program that like adds itself number after number


def fibonnaci():

    nterms = int(input("Please Input any number: "))
    # Check if number of terms is valid
    if nterms <= 0:
        print("Please, Please Enter a Positive Integer")
    else:
        print("Fibonacci Sequence: ")
        for k in range(nterms):
            print(recursion_fibo(k))

def recursion_fibo(n):
    if n <= 1:
        return n
    else: return recursion_fibo(n-1) + recursion_fibo(n-2)


print("#########+Welcome to the FIBOPro+##########")
print("This program prints out the Fibonacci series of any given number\nTRY IT OUT!!!")
while True:
    check = input("Wanna Try it Out?, if yes press[y],if press[Q] to Quit:\t")

    if (check.upper()=='Q'):
        print("Thank You, We hope to see you Try Next Time")
        break

    else:
        print("Enjoy.......")
        print()
        fibonnaci()





