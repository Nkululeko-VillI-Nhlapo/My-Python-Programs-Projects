from beautifultable import BeautifulTable






def amortize(value, rate, pmt_yrs):
    n=0
    intrate = rate / 12.0
    totalpmts = pmt_yrs * 12
    payment = (intrate * value) / (1 - pow(1 + intrate, - totalpmts))
    table = BeautifulTable()
    table.columns.header = ["MONTH", "LOAN VALUE", "PAYMENT", "INTEREST", "PRINCIPLE", "NEW VALUE"]

    while value > 0:
        n = n+1
        interest = (value * intrate)
        principle = payment - interest
        #principle = 60.6

        if value - payment < 0:
            principle = value
        table.rows.append([n, value, payment, interest, principle, value - principle])

        value = value - principle
    print(table)

amortize(1090,0.06,1)


#amount_toBorrow = float(input("Please enter your Loan Amount, e.g 1340.00:R\t"))
#rate = int(input("Please give the interest rate per annum, e.g 3%: \t%"))
#years = float(input("For how many years would you like to repay the loan?:\t"))

months = 18
annualRate = 0.06
total_Interest = 90
total_amount = 1090
m_repay = 60.6
m_repay = int(m_repay)

#for k in range(-1090, 0,m_repay):
    #print(k)






