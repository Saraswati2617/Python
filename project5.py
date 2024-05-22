'''SILENT AUCTION PROGRAM
enter bidders name, bid price and then hide it then compare all bid price and output'''

import os

def winner(auctiondict):
    max=0
    for i in auctiondict:
        price=auctiondict[i]
        if price>max:
            max=price
            person=i
    print(f"Thw winner bidder is{person} with price of {max}")



clear=False
mybiddict={}
while clear==False:
    name=input("enter your name:")
    bid=int(input("enter your bid price:"))
    mybiddict[name]=bid 
    ask=input("Do you have more bidders:Type Y for yes and N for no:-")
    if (ask=='N'):
        # print(mybiddict)
        winner(mybiddict)
        clear=True
    else:
        os.system("cls")

