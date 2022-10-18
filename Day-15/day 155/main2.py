MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

bank = resources

# balance of money is originally 0
balance = 0

restart = True
while restart:
    # prompt user and collect their input
    print("An Espresso costs: $1.50 \nA Latte costs: $2.50 \nA Cappuccino costs: $3.0 \n ")
    user_request = input("What would you like? (espresso/latte/cappuccino? : ").lower()


    # define current resources
    current_resource = f"""
    Water: {bank['water']} ml
    Milk : {bank['milk']}ml
    Coffee : {bank['coffee']}g
    Money : ${balance}
    """

    # check user input and respond accordingly
    if user_request == 'report':
        print(current_resource)

    elif user_request == 'latte' or user_request == 'cappuccino' or user_request == 'espresso':
        print("Alright, order received")
        drink = MENU[user_request]['ingredients']
        drink_price = MENU[user_request]['cost']

        # print(drink)
        # print(drink_price)

        # Check if resources are enough
        check = drink['water'] < bank['water'] and drink['milk'] < bank['milk'] and drink['coffee'] < bank['coffee']
        if check:
            print("Proceed")

            # Process the coins
            print("Please insert some coins.")
            quarters = float(input("How many quarters?")) * 0.25
            dime = float(input("How many dimes?")) * 0.10
            nickel = float(input("How many nickels?")) * 0.05
            penny = float(input("How many pennies?")) * 0.01

            total_cash = quarters + dime + nickel + penny

            if total_cash > float(drink_price):
                change = round(total_cash - float(drink_price), 2)
                print(f"Here is ${change} in change")
                print(f"Here's your {user_request} ")

                # Deduct required resource and add money to balance
                balance += drink_price
                bank['water'] -= drink['water']
                bank['milk'] -= drink['milk']
                bank['coffee'] -= drink['coffee']


            elif total_cash < float(drink_price):
                print("Your money is not enough. Money refunded ")

        else:
            not_enough = []

            if drink['water'] > bank['water']:
                not_enough.append('water')
            if drink['milk'] > bank['milk']:
                not_enough.append('milk')
            if drink['coffee'] > bank['coffee']:
                not_enough.append('coffee')

            print(f"The following resources are not enough: {not_enough}")

    elif user_request == 'off':
        restart = False

    else:
        print("invalid input, try again.")

