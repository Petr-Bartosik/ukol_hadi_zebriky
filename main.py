from player import get_player_names
from game_logic import move_player, check_winner, check_same_position
from dice import roll_dice
from intro import show_rules

show_rules()

player1, player2 = get_player_names()
pos1, pos2 = 0, 0

while True:
    input(f"{player1} háže. ENTER pro hod kostkou.")
    dice_val = roll_dice()
    print(f"{player1} hodil číslo {dice_val}")
    pos1 = move_player(player1, pos1, dice_val)
    pos2 = check_same_position(player1, pos1, player2, pos2)
    check_winner(player1, pos1)

    input(f"{player2} háže. ENTER pro hod kostkou.")
    dice_val = roll_dice()
    print(f"{player2} hodil číslo {dice_val}")
    pos2 = move_player(player2, pos2, dice_val)
    pos1 = check_same_position(player2, pos2, player1, pos1)
    check_winner(player2, pos2)
