class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.set_state('choosing_action')

    def process_user_input(self, user_input):
        if self.state == 'choosing_action':
            if user_input == 'buy':
                if self.cups < 1:
                    print("Sorry, not enough cups!")
                    self.set_state('choosing_action')
                else:
                    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
                    self.set_state('coffee_type')
            elif user_input == 'fill':
                print('Write how many ml of water you want to add: ')
                self.set_state('water_add')
            elif user_input == 'take':
                print(f'I gave you ${self.money}')
                self.money = 0
                self.set_state('choosing_action')
            elif user_input == 'remaining':
                print(f'The coffee machine has:\n'
                    f'{self.water} ml of water\n'
                    f'{self.milk} ml of milk\n'
                    f'{self.beans} g of coffee beans\n'
                    f'{self.cups} disposable cups\n'
                    f'${self.money} of money')
                self.set_state('choosing_action')
            elif user_input == 'exit':
                exit(0)
            else:
                self.set_state('choosing_action')

        elif self.state == 'coffee_type':
            self.process_coffee_type(user_input)
        elif self.state == 'water_add':
            self.water += int(user_input)
            print('Write how many ml of milk you want to add: ')
            self.set_state('milk_add')
        elif self.state == 'milk_add':
            self.milk += int(user_input)
            print('Write how many grams of coffee beans you want to add: ')
            self.set_state('beans_add')
        elif self.state == 'beans_add':
            self.beans += int(user_input)
            print('Write how many disposable cups of coffee you want to add: ')
            self.set_state('cups_add')
        elif self.state == 'cups_add':
            self.cups += int(user_input)
            self.set_state('choosing_action')

    def process_coffee_type(self, coffee_type):
        if coffee_type == '1':
            available_water = self.water // 250
            available_beans = self.beans // 16
            available_cups = min(available_water, available_beans)
            if available_cups >= 1:
                print('I have enough resources, making you a coffee!')
                self.water -= 250
                self.beans -= 16
                self.milk -= 0
                self.money += 4
                self.cups -= 1
            else:
                if available_beans == 0:
                    print('Sorry, not enough coffee beans!')
                if available_water == 0:
                    print('Sorry, not enough water!')
        elif coffee_type == '2':
            available_water = self.water // 350
            available_beans = self.beans // 20
            available_milk = self.milk // 75
            available_cups = min(available_water, available_beans)
            if available_cups >= 1:
                print('I have enough resources, making you a coffee!')
                self.water -= 350
                self.beans -= 20
                self.milk -= 75
                self.money += 7
                self.cups -= 1
            else:
                if available_beans == 0:
                    print('Sorry, not enough coffee beans!')
                if available_water == 0:
                    print('Sorry, not enough water!')
                if available_milk == 0:
                    print('Sorry, not enough milk!')
        elif coffee_type == '3':
            available_water = self.water // 200
            available_beans = self.beans // 12
            available_milk = self.milk // 100
            available_cups = min(available_water, available_beans)
            if available_cups >= 1:
                print('I have enough resources, making you a coffee!')
                self.water -= 200
                self.beans -= 12
                self.milk -= 100
                self.money += 6
                self.cups -= 1
            else:
                if available_beans == 0:
                    print('Sorry, not enough coffee beans!')
                if available_water == 0:
                    print('Sorry, not enough water!')
                if available_milk == 0:
                    print('Sorry, not enough milk!')

        self.set_state('choosing_action')

    def set_state(self, next_state):
        if next_state == 'choosing_action':
            print('Write action (buy, fill, take, remaining, exit):')
        self.state = next_state
