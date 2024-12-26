#finally.

from menu import menu, profit, resources


def machine_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = profit
    avail_dict = {"water": water, "milk": milk, "coffee": coffee, "money": money}
    return avail_dict


def beverage_report(beverage):
    milk = menu[beverage]["ingredients"]["milk"] if "milk" in menu[beverage]["ingredients"] else 0
    needed_dict = {"water": menu[beverage]["ingredients"]["water"], "milk": milk,
                   "coffee": menu[beverage]["ingredients"]["coffee"]}
    return needed_dict


def resources_sufficient(available, needed):
    result = {}
    for key in available:
        result[key] = available.get(key, 0) - needed.get(key, 0)
    for item in result:
        if result[item] < 0:
            return f"Sorry, there is not enough {item} to make this drink."
    return True


def prompt_for_coins(beverage):
    print(f"Your drink costs ${menu[beverage]['cost']:.2f}. Please insert coins.")
    coins = ["quarters", "dimes", "nickles", "pennies"]
    amounts = []
    for item in coins:
        while True:
            user_input = input(f"How many {item}? ")
            if user_input.isdigit():
                coin_count = int(user_input)
                amounts.append(coin_count)
                break
            else:
                print("That is not a valid answer. Please try again.")
    return (amounts[0] * 0.25) + (amounts[1] * 0.10) + (amounts[2] * 0.05) + (amounts[3] * 0.01)


def make_coffee(needed):
    global resources
    for key in needed:
        resources[key] = resources.get(key, 0) - needed.get(key, 0)


def transaction_successful(beverage, money):
    cost_of_beverage = menu[beverage]["cost"]
    if money < cost_of_beverage:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif money > cost_of_beverage:
        print(f"Here is your change: ${money-cost_of_beverage:.2f}")
        return True
    else:
        return True


machine_on = True
while machine_on:
    choice = input("What would you like? espresso / latte / cappuccino: ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        report = machine_report()
        print(f"Water: {report['water']}\nMilk: {report['milk']}\nCoffee: {report['coffee']}\n"
              f"Money: ${report['money']:.2f}")
    elif choice in menu:
        resources_available = machine_report()
        resources_needed = beverage_report(choice)
        sufficient = resources_sufficient(resources_available, resources_needed)
        if sufficient is True:
            coins_inserted = prompt_for_coins(choice)
            if transaction_successful(choice, coins_inserted):
                make_coffee(resources_needed)
                profit += menu[choice]["cost"]
                print(f"Here is your {choice}. Enjoy!")
        else:
            print(sufficient)
    else:
        print("That is not a valid choice. Please try again.")
