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
            "water": 400,
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
# function that prints the current resource

bank = resources

# Prompt user by asking what they would like
user_request = input("What would you like? (espresso/latte/cappuccino? : ").lower()


# add money to the resource
bank['Money'] = 0


# define function that collects drink


def collect_drink(drink):
    return MENU[drink]


if user_request == 'report':
    print(bank)
else:
    drink = collect_drink(user_request)['ingredients']
    drink_cost = collect_drink(user_request)['cost']



# Check if resources are enough


def check_resources():
    check = drink['water'] < bank['water'] and drink['milk'] < bank['milk'] and drink['coffee'] < bank['coffee']
    if check:
        return "Proceed"
    else:
        not_enough = []

        if drink['water'] > bank['water']:
            not_enough.append('water')
        if drink['milk'] > bank['milk']:
            not_enough.append('milk')
        if drink['coffee'] > bank['coffee']:
            not_enough.append('coffee')

        return f"The following resources are not enough: {not_enough}"
# Process coins


def process_coins():
    print("Please insert some coins.")
    quarters = float(input("How many quarters?")) * 0.25
    dime = float(input("How many dimes?")) * 0.10
    nickel = float(input("How many nickels?")) * 0.05
    penny = float(input("How many pennies?")) * 0.01

    total_cash = quarters + dime + nickel + penny

    if total_cash > float(drink_cost):
        change = round(total_cash - float(drink_cost), 2)
        print(f"Here is ${change} in change")
        print(f"Here's your {user_request} ")
    elif total_cash < float(drink_cost):
        print("Your money is not enough. Money refunded ")


# Define a function that makes the drink
def make_drink():
    bank['Money'] += drink_cost
    bank['water'] -= drink['water']
    bank['milk'] -= drink['milk']
    bank['coffee'] -= drink['coffee']
    return bank

Condition_to_continue = True

while Condition_to_continue:
    if user_request == 'report':
        print(bank)
        user_request = input("What would you like? (espresso/latte/cappuccino? : ").lower()
    elif user_request == 'off':
        Condition_to_continue = False
    else:
        drink = collect_drink(user_request)['ingredients']
        drink_cost = collect_drink(user_request)['cost']

    collect_drink(user_request)
    print(check_resources())



    user_request = input("What would you like? (espresso/latte/cappuccino? : ").lower()
