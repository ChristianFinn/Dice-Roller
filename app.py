import random


yes_commands = ('YES', 'YES PLEASE', 'OK')
no_commands = ('NO', 'NO THANK YOU', 'NO THANKS')


def print_dice(dice_num):
    if dice_num == 1:
        print('''\
        |-------|
        |       |
        |   0   |
        |       |
        |-------|''')
    elif dice_num == 2:
        print('''\
        |-------|
        | 0     |
        |       |
        |     0 |
        |-------|''')
    elif dice_num == 3:
        print('''\
        |-------|
        | 0     |
        |   0   |
        |     0 |
        |-------|''')
    elif dice_num == 4:
        print('''\
        |-------|
        | 0   0 |
        |       |
        | 0   0 |
        |-------|''')
    elif dice_num == 5:
        print('''\
        |-------|
        | 0   0 |
        |   0   |
        | 0   0 |
        |-------|''')
    elif dice_num == 6:
        print('''\
        |-------|
        | 0 0 0 |
        | 0 0 0 |
        | 0 0 0 |
        |-------|''')


again = True
dont_print = False


start = input('Welcome to my dice roller. Would you like to roll the dice? ').upper()
if start in yes_commands:
    again = True
    dont_print = False
elif start in no_commands:
    again = False
else:
    print('I do not understand the response....')
    again = True
    dont_print = True
while again:
    if not dont_print:
        roll = random.randint(1, 6)
        print_dice(roll)
    again_txt = input('Would you like to roll again? ').upper()
    if again_txt in yes_commands:
        again = True
        dont_print = False
    elif again_txt in no_commands:
        again = False
        print('Goodbye')
    else:
        print('I do not understand the response....')
        dont_print = True
