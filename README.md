How this code works (Coffee Machine)

This is a simple coffee machine simulator. You can order espresso, latte, or cappuccino. The machine checks if it has enough ingredients, takes your coins, and makes the coffee.

____________________________________________________________________________________________________________________________

What is used in this code
dictionary (MENU): to store drink recipes and prices

dictionary (resources): to track water, milk, coffee, and money

global variable: to update profit inside a function

while loop: to keep the machine running until turned off

if / elif / else: to handle user choices

input(): to get drink order and coins from user

print(): to show messages and reports

How the coffee machine works
Machine starts
The machine asks: "What would you like? (espresso/latte/cappuccino)"

Special commands

Type report → shows how much water, milk, coffee, and money is left

Type off → turns off the machine

When you order a drink
The machine does these steps in order:

Step 1 - Check resources
It looks at the recipe of your drink and checks if there is enough water, milk, and coffee.
If not enough → it says sorry and stops.

Step 2 - Take coins
It asks how many quarters, dimes, nickles, and pennies you insert.
Then it calculates the total money.

Step 3 - Check payment
If you paid enough → it gives you change and adds the drink cost to profit.
If not enough → it refunds your money and stops.

Step 4 - Make the drink
It removes the used ingredients from resources.
It prints: "here is your (drink name)"

Keep running
After each drink, the machine asks for a new order again.
It keeps running until someone types off.

Example of a normal game round
User types latte

Machine checks: 200ml water, 150ml milk, 18g coffee needed

Machine says: "please insert coins"

User inserts coins

Machine gives change and makes latte

Machine asks again for next order
