class CoffeeMachine:
    def __init__(self, water, milk, coffee_bean, cups, money):
        self.deposit_water = water
        self.deposit_milk = milk
        self.deposit_coffee_bean = coffee_bean
        self.deposit_cups = cups
        self.deposit_money = money
        self.do = None

    def choice(self, do):
        self.do = do
        if self.do == "buy":
            self.buy()
        elif self.do == "fill":
            self.fill()
        elif self.do == "take":
            self.take()
        elif self.do == "remaining":
            self.remaining()

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        type_coffee = str(input())
        if type_coffee == "1":
            if self.deposit_water < 250:
                print("Sorry, not enough water!")
            elif self.deposit_coffee_bean < 16:
                print("Sorry, not enough coffee beans!")
            elif self.deposit_cups < 1:
                print("Sorry, not enough cups")
            else:
                print("I have enough resources, making you a coffee!")
                self.deposit_water -= 250
                self.deposit_coffee_bean -= 16
                self.deposit_cups -= 1
                self.deposit_money += 4
        elif type_coffee == "2":
            if self.deposit_water < 350:
                print("Sorry, not enough water!")
            elif self.deposit_milk < 75:
                print("Sorry, not enough milk!")
            elif self.deposit_coffee_bean < 20:
                print("Sorry, not enough coffee beans!")
            elif self.deposit_cups < 1:
                print("Sorry, not enough cups")
            else:
                print("I have enough resources, making you a coffee!")
                self.deposit_water -= 350
                self.deposit_milk -= 75
                self.deposit_coffee_bean -= 20
                self.deposit_cups -= 1
                self.deposit_money += 7
        elif type_coffee == "3":
            if self.deposit_water < 200:
                print("Sorry, not enough water!")
            elif self.deposit_milk < 100:
                print("Sorry, not enough milk!")
            elif self.deposit_coffee_bean < 12:
                print("Sorry, not enough coffee beans!")
            elif self.deposit_cups < 1:
                print("Sorry, not enough cups")
            else:
                print("I have enough resources, making you a coffee!")
                self.deposit_water -= 200
                self.deposit_milk -= 100
                self.deposit_coffee_bean -= 12
                self.deposit_cups -= 1
                self.deposit_money += 6
        elif type_coffee == "back":
            pass
        CoffeeMachine(self.deposit_water, self.deposit_milk, self.deposit_coffee_bean, self.deposit_cups, self.deposit_money)

    def fill(self):
        self.deposit_water += int(input("Write how many ml of water you want to add:"))
        self.deposit_milk += int(input("Write how many ml of milk you want to add:"))
        self.deposit_coffee_bean += int(input("Write how many grams of coffee beans you want to add:"))
        self.deposit_cups += int(input("Write how many disposable cups you want to add:"))
        CoffeeMachine(self.deposit_water, self.deposit_milk, self.deposit_coffee_bean, self.deposit_cups, self.deposit_money)

    def take(self):
        print("I gave you ${}".format(self.deposit_money))
        self.deposit_money = "0"
        CoffeeMachine(self.deposit_water, self.deposit_milk, self.deposit_coffee_bean, self.deposit_cups, self.deposit_money)

    def remaining(self):
        print("""The coffee machine has:
        {} ml of water
        {} ml of milk
        {} g of coffee beans
        {} disposable cups
        ${} of money""".format(self.deposit_water, self.deposit_milk, self.deposit_coffee_bean, self.deposit_cups, self.deposit_money))
        CoffeeMachine(self.deposit_water, self.deposit_milk, self.deposit_coffee_bean, self.deposit_cups, self.deposit_money)


user = CoffeeMachine(400, 540, 120, 9, 550)
action = input("Write action (buy, fill, take, remaining, exit):")
while True:
    if action == "exit":
        break
    user.choice(action)
    action = input("Write action (buy, fill, take, remaining, exit):")
