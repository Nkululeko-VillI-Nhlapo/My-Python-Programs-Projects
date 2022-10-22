import random

import beautifultable
from beautifultable import BeautifulTable

class Account:
    #creating an account object
    def __init__(self, id, balance = 0, annualInterestRate = 3.4):
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate

    def getId(self):
        return self.id

    def getBalance(self):
        return self.balance

    def getAnnualInterestRate(self):
        return self.annualInterestRate

    def getMonthlyInterestRate(self):
        return self.annualInterestRate / 12

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()

table = BeautifulTable()
table.columns.header = ["                             Welcome to BalBank                                                                                                 "]
table.rows.append(['Where Your Money is Safe and Secure'])
print(table)

def bottomTable():

    tabl = BeautifulTable()
    tabl.columns.header=['                                   BalBank ATM                                   ']
    tabl.rows.append(['Thank You For choosing BalBank as your number one Bank'])
    print(tabl)


def main():
    #creating accounts
    accounts = []
    for i in range(1000, 9999):
        account =  Account(i, 0)
        accounts.append(account)


     #Atm processs
    while True:
           #getting the account pin from the user
        id = int(input('Enter Pin\t'))
            #checking the pin, and allowing the user to re-enter if the pin is incorrect
        while id < 1000 or id > 9999:
            id = int(input('\nInvalid Pin...Please ReEnter:\t'))

        while True:
             #Printing out the user menu, so that the user can choose what to do
            print('\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit')

             #allowing the user to choose any option, to transact
            selection = int(input('Enter your selection, e.g 1 = will let you view your account balance:\t'))
             #Getting account object
            for acc in accounts:
                #Comparing account id
                if acc.getId() == id:
                    accountObj = acc
                    break

            #Veiwing the balance
            if selection == 1:
                print(f"{accountObj.getBalance()} R")

            #Withdrawal
            elif selection == 2:
                #getting the withdrwal amount from the user
                amt = float(input('\n Enter amount to withdraw:\t'))
                ver_withdrwal = input(f"\n is this the correct amount {amt}?, Yes or No:\t" )

                if ver_withdrwal.upper() == 'YES':
                    print("Verify withdraw")
                else: break

                if amt < accountObj.getBalance():
                    1906#Calling withdrawal method
                    accountObj.withdraw(amt)
                    #Priniting Updated Balance
                    print(f'\nUpdated Balance: {accountObj.getBalance()} R ')

                else:
                    print(f"\n you hav insufficient money in your Account {accountObj.getBalance()} R")
                    print('\nPlease make a Deposit')

            #Deposit
            elif selection == 3:
                #getting Deposit amount from the user
                amt = float(input("\nEnter amount to deposit:\t"))
                ver_deposit = input(f"\n is this the correct amount {amt}?, Yes or No:\t")

                if ver_deposit.upper() == 'YES':
                    #Calling deposit method
                    accountObj.deposit(amt)
                    #Printing Updated Balance
                    print(f'\nUpdated Balance: {accountObj.getBalance()} R ')
                else: break

            #Exit selection
            elif selection == 4:
                print("\nTransaction is now Complete")
                print("Transaction number: " , random.randint(10000, 10000000))
                print("Current Interest Rate: ", accountObj.annualInterestRate)

                bottomTable()
                exit()

             #Any other choice other than 1,2,3,4 is Wrong
            else:
                print("ERORR, thats an invalid choice")

#Calling the function
main()




























