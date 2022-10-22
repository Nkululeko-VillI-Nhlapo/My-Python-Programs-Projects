bidding = True
auction_dict = {}

def secret_auction(name, bid):
    auction_dict[name] = bid
    if bidding == False:
        top = 0
        for highest_bid in auction_dict:
            if int((auction_dict[highest_bid])) > int(top):
                top = int((auction_dict[highest_bid]))
                win_name = highest_bid


if bidding == True:
    print("We Selling Huawei Y9 2019 \n Welcome to the Secret Auction Program")
    name = input("What is your name?: ")
    bid = int(input("What's your Bid: R"))
    secret_auction(name, bid)
    other_bid = input("Are there any other bidders? Type 'Yes or No.'\n".lower())

while other_bid =='yes':
    name = input("What is your name?: ")
    bid = int(input("What's your Bid: R"))
    secret_auction(name, bid)
    other_bid = input("Are there any other bidders? Type 'Yes or No.\n".lower())

if other_bid == 'no':
    bidding = False
    secret_auction(name, bid)







