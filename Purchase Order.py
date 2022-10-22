def items_slip(items):
    if len(items) < 1:
        print("Thank You, we hope to see you make a purchase in the near future")
    else:
        print()
        summation = sum(list(items.values()))


        items['total'] = summation
        for key,value in items:
            print(key, ':',value)
        print()
    maximo(max)
def maximo(max):
    items.pop('total')

    max_price = list(items.values())
    max_item = list(items.keys())
    result = max_item[max_price.index(max(max_price))]
    most_expensive = max(max_price)
    print(f"The most expensive item is {result}  with a price of R{most_expensive}")
    average()
def average():
    print()
    summation = sum(list(items.values()))
    num_valuesInItems = len(items)

    averagePrice = summation / num_valuesInItems
    averagePrice = round(averagePrice)

    print(f"The average price in the list is R{averagePrice}")

items = {}
choice = ''

while True:
    choice = input("Do you want to purchase something, answer in [y/n]: \t")

    if (choice.lower() == 'n'):
        items_slip(items)
        break

    else:
        item = input("Please Enter the item you want to buy, e.g Koo Baked Beans: \t")
        price = float(input("Please enter the price of the item, e.g 5 means R5: \tR"))

        items[item] = price
        print()




