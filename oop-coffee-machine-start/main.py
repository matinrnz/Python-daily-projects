from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
machine_execution = True
# Create objects of Menu, Coffee Maker  and Money Machine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while machine_execution:
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    order_name = input(f"What would you like? ({menu.get_items()}): ")
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if order_name == "off":
        machine_execution = False
    # TODO: 3.  Print report.
    elif order_name == "report":
        # Call the report method on the objects
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(order_name)
        # TODO: 4. Check resources sufficient?
        if coffee_maker.is_resource_sufficient(order):
            # TODO: 5. Process coins.
            # TODO: 6. Check transaction successful?
            cost = order.cost
            if money_machine.make_payment(cost):
                # TODO: 7.  Make Coffee.
                coffee_maker.make_coffee(order)






