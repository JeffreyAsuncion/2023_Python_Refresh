# import random
# define a function to roll the dice
# create a dictory that will have the drawing of the dice

import random
import string


dice_drawing = {
    1: (
        "+---------+",
        "|         |",
        "|    1    |",
        "|         |",
        "+---------+"
        ),
    2: (
        "+---------+",
        "|         |",
        "|    2    |",
        "|         |",
        "+---------+"
        
        ),
    3: (
        "+---------+",
        "|         |",
        "|    3    |",
        "|         |",
        "+---------+"
        
        ),
    4: (
        "+---------+",
        "|         |",
        "|    4    |",
        "|         |",
        "+---------+"
        ),
    5: (
        "+---------+",
        "|         |",
        "|    5    |",
        "|         |",
        "+---------+"
        ),
    6: (
        "+---------+",
        "|         |",
        "|    6    |",
        "|         |",
        "+---------+"
        ),
}

def roll_dice():
    
    roll = input("Roll the dice? (Yes/No) : ")
    
    while roll.lower() == "yes":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"dice rolled: {dice1}, {dice1}")
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        roll = input("Roll the dice? (Yes/No) : ")
    
    print("Goodbye!")

roll_dice()
