from random import randint

def roll_dice(number = 1, sides = 20):
    result = 0

    for i in range(0, number):
        result += randint(1, sides)

    return result

def generate_new_character():
    # rolles six sets of 3d6 dice and supplies them as stats
    # in dictionary forma

    character = {}

    character['STR'] = roll_dice(3, 6)
    character['DEX'] = roll_dice(3, 6)
    character['CON'] = roll_dice(3, 6)
    character['WIS'] = roll_dice(3, 6)
    character['INT'] = roll_dice(3, 6)
    character['CHA'] = roll_dice(3, 6)

    return character

def generate_new_character2():

    character = {}
    stats = ['STR', 'DEX', 'CON', 'WIS', 'INT', 'CHA']

    for stat in stats:
        character[stat] = roll_dice(3, 6)

    return character

def generate_new_character3():

    character = {
        'STR': roll_dice(3, 6),
        'DEX': roll_dice(3, 6),
        'CON': roll_dice(3, 6),
        'WIS': roll_dice(3, 6),
        'INT': roll_dice(3, 6),
        'CHA': roll_dice(3, 6)
    }

    return character

character = generate_new_character()
print(character)