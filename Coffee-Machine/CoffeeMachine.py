MENU = {
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost": 1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":18,
        },
        "cost": 2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water":150,
            "milk":130,
            "coffee":18,
        },
        "cost": 3.0,
    },

}
resources = {
    "water":400,
    "milk":400,
    "coffee":100,
    "money": 0,
}
profit = 0



def resources_check(order_ingredients):

    '''check if resources are available'''

    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:

            print(f"SORRY THER IS NOT ENOUGH {item}")
            return False
    return True



def process_coins():

    ''' Returns the total calculate coins inserted'''

    print("pleas insert coins")
    total =int(input("How meany quarters?")) * 0.25
    total +=int(input("How meany dimes?")) * 0.1
    total +=int(input("How meany nickles?")) * 0.05
    total +=int(input("How meany pennies?")) * 0.01
    return total



def is_enough_money(money_recived, drink_cost):

    '''Returns True if money is enough and Returns False if money isn't enough'''

    if money_recived >= drink_cost:

        change = round(money_recived - drink_cost, 2)
        print(f"here is ${change}change.")
        global profit
        profit += drink_cost
        return True

    else:

        print("Sorry its not enough money . money refunded")
        return False

# Remove used ingredients from resources and serve the drink

def make_cofee(drink_name, order_ingredients):

    '''deduct the requierd ingredients from the resources'''

    for item in order_ingredients:

        resources[item] -= order_ingredients[item]
    print(f"here is youre {drink_name}")

machine_is_on = True



while machine_is_on:

    user_input = input("What would you like? (espresso/latte/cappuccino)\n").lower()

    

    if user_input == "off":

        machine_is_on = False

    

    elif user_input == "report":

       print(f"water:{resources['water']}ml")
       print(f"Milk:{resources['milk']}ml")
       print(f"Coffee:{resources['coffee']}gr")
       print(f"Money:{profit}")
    else:

        drink = MENU[user_input]

        

        if resources_check(drink["ingredients"]) is True:

            payment = process_coins()

            if is_enough_money(payment, drink["cost"]):

                make_cofee(user_input, drink["ingredients"])
