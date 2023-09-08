from menu import MENU, resources

is_on = True
total_money_entered = 0

def take_order():
    order = input("What would you like? (espresso/latte/cappuccino): ")
    return order

def check_resources(order):
    if resources["water"] < MENU[order]["ingredients"]["water"]:
        return "water"
    if resources["coffee"] < MENU[order]["ingredients"]["coffee"]:
        return "coffee"
    if order == "latte" or order == "cappuccino":
        if resources["milk"] < MENU[order]["ingredients"]["milk"]:
            return "milk"
    return "enough"

def process_coins(order):
    global total_money_entered
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies: "))
    total_money_entered = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    if order == "espresso":
        if total_money_entered < MENU["espresso"]["cost"]:
            return "not enough"
        elif total_money_entered > MENU["espresso"]["cost"]:
            return "give change"
    elif order == "latte":
        if total_money_entered < MENU["latte"]["cost"]:
            return "not enough"
        elif total_money_entered > MENU["latte"]["cost"]:
            return "give change"
    elif order == "cappuccino":
        if total_money_entered < MENU["cappuccino"]["cost"]:
            return "not enough"
        elif total_money_entered > MENU["cappuccino"]["cost"]:
            return "give change"
    else:
        return "enough"

def calculate_change(order, money_entered):
    change = money_entered - MENU[order]["cost"]
    return change

def work():
    global is_on
    order = take_order()
    if order == "report":
        print(f'Resources: water: {resources["water"]}ml, milk: {resources["milk"]}ml, coffee: {resources["coffee"]}g, money: £{resources["money"]}')
    elif order == "off":
        is_on = False
    else:
        enough_resources = check_resources(order)
        if enough_resources != "enough":
            is_on = False
            print(f"Sorry, there is not enough {enough_resources} for your order.")
        else:
            enough_coins = process_coins(order)
            if enough_coins == "not enough":
                is_on = False
                print("Sorry, you have not entered enough money. Money refunded")
            else:
                if enough_coins == "give change":
                    change = round(calculate_change(order, total_money_entered), 2)
                    print(f"Here is your change: ${change}")
                resources["money"] += MENU[order]["cost"]
                resources["water"] -= MENU[order]["ingredients"]["water"]
                if order == "latte" or order == "cappuccino":
                    resources["milk"] -= MENU[order]["ingredients"]["milk"]
                resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
                print(f"Here is your {order}☕. Enjoy!")

while is_on:
    work()