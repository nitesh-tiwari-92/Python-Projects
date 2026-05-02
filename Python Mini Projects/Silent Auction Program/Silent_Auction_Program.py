

import os

print(' Welcome to the Silent Auction Program '.center(100, '*'))

bids = {}
other_bid = 'yes'

def check_user_name():

    name = input('\nWhat is Your Name? ').title()

    if name in bids:
        print(f'\nUser Name {name} already available, please input different name!')
        return check_user_name()

    else:
        return name


while other_bid in ['yes', 'ye', 'y']:

    user_bid = 0
    user_name = check_user_name()

    while user_bid <= 0:        
        try:
            user_bid = int(input('What is your Bid? '))

            if user_bid > 0:
                bids.update({user_name: user_bid})

            else:
                print('\nBid Should be greater than 0.')

        except:
            print('\nInvalid Input. Please provide your Bid in NUmbers only!')

    other_bid = input('\nAre there any other bidders? Type \'Yes\' or \'No\': ').lower()
    os.system('cls')

for k, v in bids.items():
    if v >= user_bid:
        user_bid = v
        user_name = k

print(f'\nBidder {user_name.title()} with {user_bid} Bids won the Auction.')
