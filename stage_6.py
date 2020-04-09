class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, disposable_cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.money = money
        self.disposable_cups = disposable_cups
        self.action = None
        self.buy_status = None

    def check_able(self, other):
        if self.water < other.water:
            print("Sorry, not enough water!" "\n")
        elif self.milk < other.milk:
            print("Sorry, not enough milk!" "\n")
        elif self.coffee_beans < other.coffee_beans:
            print("Sorry, not enough coffee beans!" "\n")
        elif self.disposable_cups < other.disposable_cups:
            print("Sorry, not enough disposable cups!" "\n")
        else:
            print("I have enough resources, making you a coffee!" '\n')
            self.water -= other.water
            self.milk -= other.milk
            self.coffee_beans -= other.coffee_beans
            self.disposable_cups -= other.disposable_cups
            self.money += other.money

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.coffee_beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:" '\n')
        self.disposable_cups += int(input())

    def remaining(self):
        print(f'''The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.disposable_cups} of disposable cups
${self.money} of money''', '\n')

    def take_money(self):
        print(f"I gave you ${self.money}", '\n')
        self.money = 0

    def menu(self):
        while self.action != "exit":
            self.action = input("Write action (buy, fill, take, remaining, exit):\n")
            print()
            if self.action == "buy":
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                self.buy_status = input()
                if self.buy_status == "1":
                    my_coffee.check_able(espresso)
                elif self.buy_status == "2":
                    my_coffee.check_able(latte)
                elif self.buy_status == "3":
                    my_coffee.check_able(cappuccino)
                elif self.buy_status == "back":
                    self.menu()
                self.menu()
            elif self.action == "fill":
                self.fill()
            elif self.action == "take":
                self.take_money()
            elif self.action == "remaining":
                self.remaining()
            elif self.action == "exit":
                exit(0)

                
cappuccino = CoffeeMachine(200, 100, 12, 1, 6)
latte = CoffeeMachine(350, 75, 20, 1, 7)
espresso = CoffeeMachine(250, 0, 16, 1, 4)
my_coffee = CoffeeMachine(400, 540, 120, 9, 550)
CoffeeMachine.menu(my_coffee)

