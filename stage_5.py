def have_printer():
    print(f'''The coffee machine has:
{machine_list[0]} of water
{machine_list[1]} of milk
{machine_list[2]} of coffee beans
{machine_list[3]} of disposable cups
${machine_list[4]} of money''', '\n')
def action_buy():
    buy_list = {1: [250, 0, 16, 1, -4], 2: [350, 75, 20, 1, -7], 3: [200, 100, 12, 1, -6]}
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    buy_number = input()
    if buy_number == 'back':
        return
    resource_status = 1
    for i in range(len(machine_list)):
        if machine_list[i] - buy_list[int(buy_number)][i] < 0:
            print(f"Sorry, not enough {resource_list[i]}!")
            resource_status = 0
            print()
    if resource_status == 1:
        for i in range(len(machine_list)):
           machine_list[i] = machine_list[i] - buy_list[int(buy_number)][i]
        print("I have enough resources, making you a coffee!")
        print()

def action_move(action):
    if action == 'buy':
        action_buy()
    elif action == 'fill':
        print("Write how many ml of water do you want to add:")
        machine_list[0] += int(input())
        print("Write how many ml of milk do you want to add:")
        machine_list[1] += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        machine_list[2] += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        machine_list[3] += int(input())
        print()
    elif action == 'take':
        print(f"I gave you ${machine_list[4]}", '\n')
        machine_list[4] = 0
    elif action == 'remaining':
        if machine_list[4] > 0:
            have_printer()
        else:
            print(f'''The coffee machine has:
{machine_list[0]} of water
{machine_list[1]} of milk
{machine_list[2]} of coffee beans
{machine_list[3]} of disposable cups
{machine_list[4]} of money''', '\n')


water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550
resource_list = ["water", "milk", "coffee_beans", "disposable_cups", 'money']
machine_list = [water, milk, coffee_beans, disposable_cups, money]

print("Write action (buy, fill, take, remaining, exit):")
action = input()
print()
action_move(action)
while action != 'exit':
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    print()
    action_move(action)

# espresso = [250, 0, 16, 1, -4]
# latte = [350, 75, 20, 1, -7]
# cappuccino = [200, 100, 12, 1, -6]

# print("Write how many ml of water the coffee machine has:")
# water = int(input())
# print("Write how many ml of milk the coffee machine has:")
# milk = int(input())
# print("Write how many grams of coffee beans the coffee machine has:")
# beans = int(input())
# def check_coffee():
#     print("Write how many cups of coffee you will need:")
#     cups = int(input())
#     values_list = [water // 200, milk // 50, beans // 15]
#     act_cups = min(values_list)
#     if act_cups == cups:
#         print("Yes, I can make that amount of coffee")
#     elif act_cups < cups:
#         print(f"No, I can make only {act_cups} cups of coffee.")
#     elif act_cups > cups:
#         print(f"Yes, I can make that amount of coffee (and even {act_cups - cups} more than that)")
# check_coffee()


