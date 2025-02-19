#volani vsech modulu-->vystup

from player import players_name
from game_logic import move_player, check_winner, check_same_position
from dice import roll_dice
from intro import show_rules

# ANSI barvy pro rozlišení hráčů
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"


show_rules()#ukazat pravidla (import z intro)

player1, player2 = players_name()#volani hracu = jmena

pos1, pos2 = 0, 0 #pozice pri startu

while True:
    #______________________________1. hrac________________________________________________________________________________
    input(f"{RED}{player1}{RESET} háže. ENTER pro hod kostkou.")
    dice_val = roll_dice() #hod kostkou
    print(f"{RED}{player1}{RESET} hodil číslo {dice_val}")

    pos1 = move_player(RED + player1 + RESET, pos1, dice_val)#posunuti prvniho hrace
    pos2 = check_same_position(RED + player1 + RESET, pos1, BLUE + player2 + RESET, pos2)#kontrola check same position = KOLIZE

    check_winner(RED + player1 + RESET, pos1)#kontrola výhry
    #______________________________2. hrac________________________________________________________________________________
    input(f"{BLUE}{player2}{RESET} háže. ENTER pro hod kostkou.")
    dice_val = roll_dice()#hod kostkou
    print(f"{BLUE}{player2}{RESET} hodil číslo {dice_val}")

    pos2 = move_player(BLUE + player2 + RESET, pos2, dice_val)#posunuti druheho hrace
    pos1 = check_same_position(BLUE + player2 + RESET, pos2, RED + player1 + RESET, pos1)#check kolize

    check_winner(BLUE + player2 + RESET, pos2)#check vyhry

