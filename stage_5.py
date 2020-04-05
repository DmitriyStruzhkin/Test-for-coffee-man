# Write your code here
# print("Write how many cups of coffee you will need:")
# cups = int(input())
# print(f'''For {cups} cups of coffee you will need:
# {cups * 200} ml of water
# {cups * 50} ml of milk
# {cups * 15} g of coffee beans''')
def have_printer():
    print(f'''The coffee machine has:
{machine_list[0]} of water
{machine_list[1]} of milk
{machine_list[2]} of coffee beans
{machine_list[3]} of disposable cups
{machine_list[4]} of money''', '\n')

def action_move(action):
    buy_list = {1: [250, 0, 16, 1, -4], 2: [350, 75, 20, 1, -7], 3: [200, 100, 12, 1, -6]}
    if action == 'buy':
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        buy_number = int(input())
        for i in range(len(machine_list)):
            machine_list[i] = machine_list[i] - buy_list[buy_number][i]
            print(machine_list[i], buy_list[buy_number][i])
        have_printer()
    elif action == 'fill':
        print("Write how many ml of water do you want to add:")
        machine_list[0] += int(input())
        print("Write how many ml of milk do you want to add:")
        machine_list[1] += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        machine_list[2] += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        machine_list[3] += int(input())
        have_printer()
    elif action == 'take':
        print(f"I gave you ${machine_list[4]}", '\n')
        machine_list[4] = 0
        have_printer()

water = 1200
milk = 540
beans = 120
dis_caps = 9
money = 550
machine_list = [water, milk, beans, dis_caps, money]

have_printer()

print("Write action (buy, fill, take):")
action = input()
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


