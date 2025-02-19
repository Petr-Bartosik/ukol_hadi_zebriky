from player import get_player_names
from game_logic import move_player, check_winner, check_same_position
from dice import roll_dice
from intro import show_rules

# ANSI barvy pro rozlišení hráčů
from player import get_player_names
from game_logic import move_player, check_winner, check_same_position
from dice import roll_dice
from intro import show_rules

# ANSI barvy pro rozlišení hráčů
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

show_rules()

player1, player2 = get_player_names()

pos1, pos2 = 0, 0

while True:
    input(f"{RED}{player1}{RESET} háže. ENTER pro hod kostkou.")
    dice_val = roll_dice()
    print(f"{RED}{player1}{RESET} hodil číslo {dice_val}")
    pos1 = move_player(RED + player1 + RESET, pos1, dice_val)
    pos2 = check_same_position(RED + player1 + RESET, pos1, BLUE + player2 + RESET, pos2)
    check_winner(RED + player1 + RESET, pos1)

    input(f"{BLUE}{player2}{RESET} háže. ENTER pro hod kostkou.")
    dice_val = roll_dice()
    print(f"{BLUE}{player2}{RESET} hodil číslo {dice_val}")
    pos2 = move_player(BLUE + player2 + RESET, pos2, dice_val)
    pos1 = check_same_position(BLUE + player2 + RESET, pos2, RED + player1 + RESET, pos1)
    check_winner(BLUE + player2 + RESET, pos2)

