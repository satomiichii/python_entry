from data import MENU, resources, unit

power = True


def check_resource(user_drink):
    """This function checks if there is enogh resourse to make user's choice drink."""
    for ingredient in user_drink['ingredients']:
        if resources[ingredient] < user_drink['ingredients'][ingredient]:
            print(f'Sorry there is not enough {ingredient}.')
            return False
    return True


while power:
    command = input("What would you like? (espresso/latte/cappuccino): ")

    if command == 'off':
        power = False
    elif command == 'report':
        for item in resources:
            item_title = item.title()
            if item == 'money':
                print(f"{item_title}: {unit[item]}{resources[item]}")
            else:
                print(f"{item_title}: {resources[item]}{unit[item]}")
    else:
        drink = MENU[command]
        price = float(drink['cost'])
        enough_resource = check_resource(drink)

        if enough_resource:
            coins = 0
            print('Please insert coins.')
            coins += float(input('how many quarters?: ')) * 0.25
            coins += float(input('how many dimes?: ')) * 0.10
            coins += float(input('how many nickles?: ')) * 0.05
            coins += float(input('how many pennies?: ')) * 0.01

            if coins < drink['cost']:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = round(coins - price, 2)
                print(f'Here is ${change} in change.')
                print(f'Here is your {command} ☕️. Enjoy!')
                if 'money' in resources:
                    resources['money'] += price
                else:
                    resources['money'] = price

                for ingredient in drink['ingredients']:
                    resources[ingredient] -= drink['ingredients'][ingredient]



