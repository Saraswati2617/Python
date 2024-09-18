'''COFFEE MACHINE'''
'''STEPS:-
1.Ask from user for coffee type by prompting:
"what would you like to have?(latte/espresso/cappuccino)?:
Once the drink is dispensed this prompt should be shown to serve the next customer.
2.When user enters "report" as an input then a report should be generated that shows the current resources value:
  eg:Water=200ml
     milk=50ml
     coffee=75g
     money=rs.150
3.If user enters "off" as an input then your program should end execution.
4.Check sufficient resources are available or not.
5.If sufficient resources are available then machine should ask to insert coins and calculate total money received.
  [Coffee machine only accept 5rs. , 10rs. , 20rs. coins]
6.Check payment is successful or not
  If user has entered too much money,the cost of drink gets added to the machine as profit.
  If money is not sufficient to purchase the drink user has selected,it should print a message "Sorry,That's not enough money.Money refunded"
7.Make coffee
If payment is successful,ingredients to make the selected drink should be deducted from the coffee machine resources.And it will print a message
"Here is your cappacino"     '''


def check_resources(ingredients):
  for item in ingredients:
    if ingredients[item]>resources[item]:
      print(f"Sorry , not enought resource available for {item}")
      return False
  return True

def process_coins():
  print("Please enter your coins")
  totalmoney=0
  coins_five=5*int(input("How many Rs.5 coins?"))
  coins_ten=10*int(input("How many Rs.10 coins?"))  
  coins_twenty=20*int(input("How many Rs.20 coins?"))
  totalmoney=coins_five+coins_ten+coins_twenty
  return totalmoney

def payment_success(payment,cost):
  if payment>=cost:
    global profit
    profit+=payment
    change=payment-cost
    print(f"Here's your {change} as change")
    return True
  else:
    print("Sorry,that's not enough money.Money refunded")
    return False

def makecoffee(ask,ingredients):
  for item in ingredients:
    resources[item]-=ingredients[item]
  print(f"Here's your {ask} '\U00002615' ....... Enjoy")

import project9db
resources = {
    "water": 1000,
    "coffee": 500,
    "milk": 2500,
}
# profit=the total money collected from users without accounting for ingredient costs.
profit=0
on=True
while on:
  ask=input("What would you like to have(Espresso\Americano\Latte\Cappuccino\Mocha\Macchiato)?:\nTo off the machine enter \"off\" \nTo print resources enter \"report\":-")
  if ask=="off":
    on=False
    print("Turning Off")
  elif ask=="report":
    print(f'water={resources["water"]}ml\nmilk={resources["milk"]}ml\ncoffee={resources["coffee"]}g')
    print(f'Money=Rs.{profit}')
  else:
    coffee=project9db.coffee_menu[ask]
    print(coffee)
    if check_resources(coffee["ingredients"])==True:
      payment=process_coins()
      if payment_success(payment,coffee["cost"])==True:
        makecoffee(ask,project9db.coffee_menu[ask]["ingredients"])