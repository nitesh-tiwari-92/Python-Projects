



import os
from time import sleep


def coin_conversion(statement):    
    rs_coin = input(statement)
    while True:
        try:
            return int(rs_coin)
        except:
            print('Invalid Input')
            return coin_conversion(statement)


def coins():
    print('\nPlease insert coins.')
    rs_5_coin = coin_conversion('\nHow many 5 Rs. coins: ')
    rs_10_coin = coin_conversion('\nHow many 10 Rs. coins: ')
    rs_20_coin = coin_conversion('\nHow many 20 Rs. coins: ')
    return rs_5_coin, rs_10_coin, rs_20_coin


def coffee_machine(coffee_price, user_input):
    total_amount_coin_inserted = 0
    money_in_wallet = 0

    while total_amount_coin_inserted <= coffee_price:
        
        print(f'\nTotal Paid Amount: {total_amount_coin_inserted}')
        rs_5_coin, rs_10_coin, rs_20_coin = coins()
        total_amount_coin_inserted += ((rs_5_coin * 5) + (rs_10_coin * 10) + (rs_20_coin * 20))

        if total_amount_coin_inserted >= coffee_price:
            price_difference = total_amount_coin_inserted - coffee_price
            print(f'\nTotal Paid Amount: {total_amount_coin_inserted}')
            money_in_wallet += total_amount_coin_inserted

            if price_difference != 0:
                print(f"\nHere is your Rs.{price_difference} in change")
                money_in_wallet -= price_difference
            break
        else:
            print(f'\nPlease pay Rs.{coffee_price - total_amount_coin_inserted} more for {user_input}')

    print(f'\nHere is your {user_input}')
    sleep(5)
    return money_in_wallet


milk_quantity = 1500
water_quantity = 3000
coffee_quantity = 500
money_in_wallet = 250
latte_price = 150
espresso_price = 200
cappucino_price = 175

while True:

    user_choice = (input("\nWhat would you like to have? (latte/espresso/cappucino): ").lower()).strip()

    if milk_quantity >= 0 and water_quantity >= 0 and coffee_quantity >= 0:

        if user_choice in ['latte', 'espresso', 'cappucino']:
            if user_choice in ('latte'):
                coffee_machine(latte_price, user_choice)
                milk_quantity -= 125
                water_quantity -= 250
                coffee_quantity -= 25
                money_in_wallet += latte_price
                os.system('cls')

            elif user_choice in ('espresso'):
                coffee_machine(espresso_price, user_choice)
                milk_quantity -= 250
                water_quantity -= 150
                coffee_quantity -= 50
                money_in_wallet += espresso_price
                os.system('cls')

            else:
                coffee_machine(cappucino_price, user_choice)
                milk_quantity -= 300
                water_quantity -= 175
                coffee_quantity -= 35
                money_in_wallet += cappucino_price
                os.system('cls')

        elif user_choice == 'off':
            exit()

        elif user_choice == 'report':
            print(f'\nMilk = {milk_quantity}ml.')
            print(f'Water = {water_quantity}ml.')
            print(f'Coffee = {coffee_quantity}g.')
            print(f'Money = Rs.{money_in_wallet}')
    else:
        print('Please refill the tanks to continue!')
