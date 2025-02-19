#hazeni kostkou

import random, time

#prodleva
waiting = 1

#počet stran kostky
sides_of_dice = 6

def roll_dice():
    time.sleep(waiting) #pauza pred hodem
    total = 0
    sides_of_dices = { #hrave tvoreni
        1: "\n   ●\n",
        2: "●\n\n    ●",
        3: "●\n  ●\n    ●",
        4: "●   ●\n\n●   ●",
        5: "●   ●\n  ●\n●   ●",
        6: "●   ●\n●   ●\n●   ●"
    }
    while True:
        roll = random.randint(1, sides_of_dice) #random cislo 1-6(sides of dice)

        print(f"Hozeno: \n{sides_of_dices[roll]}") #vizual
        total += roll #pricteni hozene hodnoty k SOUCTU

        if roll != 6: #pokud jine cislo nez 6 = break hazeni
            break
        print("Hodil jsi šestku. Tak hážeš ještě jednou.")
    return total #vratka vsech hodu (soucet)


