MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_resources(available_resources, available_money):
    """Generate a string summarizing the current resources and money in machine."""
    resource_string = ""
    for resource in available_resources:
        amount = available_resources[resource]
        resource = resource.title()
        resource_string += f"{resource}: {amount}\n"
    money_string = f"Money: ${available_money:.2f}"
    return resource_string + money_string


def get_resources(drink):
    """Retrieve list of ingredients required for selected drink."""
    for item in MENU:
        if drink == item:
            inner_dict = MENU[item]
            if 'ingredients' in inner_dict:
                return inner_dict['ingredients']


def check_resources_sufficient(drink, machine):
    """Check if there are enough resources to make selected drink."""
    for item in drink:
        new_amount = machine[item] - drink[item]
        if new_amount < 0:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Process and calculate the total value of coins inserted by the user."""
    print("Please insert your coins.")
    quarters = int(input("How many quarters? "))*0.25
    dimes = int(input("How many dimes? "))*0.10
    nickles = int(input("How many nickles? "))*0.05
    pennies = int(input("How many pennies? "))*0.01
    total = quarters + dimes + nickles + pennies
    return total


def check_transaction_successful(chosen_drink, coins_inserted):
    """Check if the user's payment is sufficient for the chosen drink."""
    for item in MENU:
        if item == chosen_drink:
            menu_item = MENU[item]
            cost_of_item = menu_item['cost']
            print(f"The cost was ${cost_of_item:.2f}")
            print(f"You paid ${coins_inserted:.2f}")
            if coins_inserted < cost_of_item:
                print("Sorry, that's not enough money. Money refunded.")
                return False
            else:
                change = abs(cost_of_item-user_coins)
                if change != 0:
                    print(f"Here is ${change:.2f} in change.")
                return cost_of_item


def adjust_resources(drink, machine):
    """"Update the machine's resources after preparing a drink."""
    for item in drink:
        if item in machine:
            new_amount = machine[item] - drink[item]
            machine[item] = new_amount


# main loop starts here
machine_on = True
while machine_on:
    # if drink chosen, determine how many resources needed to make drink
    choice = input("What would you like? Espresso/latte/cappuccino: ").lower()
    drink_dict = get_resources(choice)

    # if drink not chosen, follow appropriate instructions
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(print_resources(resources, profit))

    # check if machine has enough resources to make drink
    elif check_resources_sufficient(drink_dict, resources):

        # if yes, ask user to insert coins
        user_coins = process_coins()

        # check if the transaction was successful
        cost = check_transaction_successful(choice, user_coins)
        if cost:

            # adjust amount of money in machine
            profit += cost

            # adjust amount of resources in machine
            adjust_resources(drink_dict, resources)

            # give drink
            print(f"Here is your {choice}. ☕ Enjoy!")
        else:
            pass
    else:
        pass
