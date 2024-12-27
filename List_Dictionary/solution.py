# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from platform import system
from os import system, name

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')

run_bid=True
bid_dict={}
next_bidder=False
while run_bid:
    name=input("what is your name: ")
    price=input("what is your bid amount: ₹")
    bid_dict[name]=price
    next_bidder= input("any more bidder if continue then type Y else N ")
    if next_bidder == "Y":
        run_bid = True
        print("\n" * 20)
        #below not working in Pycharm env
        #clear()
    else:
        run_bid=False


h_name=""
h_amount=0
c_name=""
d_bid=0
for key in bid_dict:
    d_bid=int(bid_dict[key])
    if d_bid > h_amount:
        h_amount=d_bid
        c_name=key
print(f"highest Bidder name {c_name} and bidding amount {h_amount}")

