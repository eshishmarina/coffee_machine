from coffee_machine import CoffeeMachine

initial_water = 400
initial_milk = 540
initial_beans = 120
initial_cups = 9
initial_money = 550

coffee_machine = CoffeeMachine(initial_water, initial_milk, initial_beans, initial_cups, initial_money)

while True:
    coffee_machine.process_user_input(input())

