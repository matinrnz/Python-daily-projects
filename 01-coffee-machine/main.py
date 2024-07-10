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


# TODO: 4. Check resources sufficient?
def resource_checker(order):
    for item in MENU[order]['ingredients'] and resources:
        if resources[item] < MENU[order]['ingredients'][item]:
            print(f"Sorry there is not enough {item}.")
            return
        else:
            return True


# TODO: 5. Process coins.
def payment():
    print("Please insert coins.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
    # Value of each coin
    quarters_value = 0.25
    dimes_value = 0.10
    nickles_value = 0.05
    pennies_value = 0.01
    value = quarters * quarters_value + dimes * dimes_value + nickles * nickles_value + pennies * pennies_value
    return value

# TODO: 6. Check transaction successful?
def transaction():
    paid = payment()
    if paid < MENU[order]['cost']:
        print("Sorry that's not enough money. Money refunded.")
    else:
        if resource_checker(order):
            print(f"Here is ${round((paid-MENU[order]['cost']), 2)} dollars in change.")
            print(f"Here is your {order}☕. Enjoy!")
            for item in MENU[order]['ingredients'] and resources:
                resources[item] -= MENU[order]['ingredients'][item]
            return True


# TODO: 7.  Make Coffee.
machine_execution = True
profit = 0
while machine_execution:
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    order = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if order == "off":
        machine_execution = False

    # TODO: 3.  Print report.
    elif order == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: {profit}")

    else:
        if resource_checker(order):
            if transaction():
                profit += MENU[order]['cost']












