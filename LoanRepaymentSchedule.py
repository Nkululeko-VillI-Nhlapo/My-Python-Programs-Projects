from beautifultable import BeautifulTable

n = 0

print("Hello,This the Loan Repayment Schedule CalculATOR")



amount_toBorrow = int(input("Please enter your Loan Amount, e.g 1340.00:R\t"))
rate = int(input("Please give the interest rate per annum, e.g 3%: \t%"))
years = float(input("For how many years would you like to repay the loan?:\t"))


print(f'This is the amount you want to borrow: {amount_toBorrow}')

months = years * 12

annualRate = (rate/100)/12
monthly_paym = (annualRate * amount_toBorrow) / (1 - pow(1 + annualRate, -months))
#monthly_paym = 60.6
total_Interest = amount_toBorrow * (rate/100) * years
total_amountOwed = amount_toBorrow + total_Interest
table = BeautifulTable()
table.columns.header = ["Months", "AmountPaid", "Remaining Balance"]
table.rows.append([0,0,total_amountOwed])
print(f'This the total interest paid: {total_Interest}')
while total_amountOwed > 0:

    n = n+1

    interest = (total_amountOwed * annualRate)
    #amountPaid = monthly_paym - interest
    amountPaid = monthly_paym

    if total_amountOwed - monthly_paym <0:
        amountPaid = total_amountOwed
    table.rows.append([n, monthly_paym, total_amountOwed - amountPaid])

    total_amountOwed = total_amountOwed - amountPaid

print(table)




