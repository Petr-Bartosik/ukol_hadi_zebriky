import random, time

SLEEP_BETWEEN_ACTIONS = 1
DICE_FACE = 2

def roll_dice():
    time.sleep(SLEEP_BETWEEN_ACTIONS)
    total = 0
    dice_faces = {
        1: "\n   ●\n",
        2: "●\n\n    ●",
        3: "●\n  ●\n    ●",
        4: "●   ●\n\n●   ●",
        5: "●   ●\n  ●\n●   ●",
        6: "●   ●\n●   ●\n●   ●"
    }  # Lepší čitelnost pro zobrazení hodnot kostky
    while True:
        roll = random.randint(1, DICE_FACE)
        print(f"Hozeno: \n{dice_faces[roll]}")
        total += roll
        if roll != 6:
            break
        print("Hodil jsi šestku. Tak hážeš ještě jednou.")
    return total


