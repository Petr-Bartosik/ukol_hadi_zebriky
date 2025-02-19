import sys
from game_board import get_snakes, get_ladders

MAX_VAL = 100

def move_player(player, pos, dice_val):
    old_pos = pos
    pos += dice_val
    if pos > MAX_VAL:
        print(f"{player} potřebuje {MAX_VAL - old_pos} k vítězství. Zkus to znova.")
        return old_pos
    snakes, ladders = get_snakes(), get_ladders()
    if pos in snakes:
        new_pos = snakes[pos]
        print(f"{player} kousl had, propadáš se z {pos} na {new_pos}")
        pos = new_pos
    elif pos in ladders:
        new_pos = ladders[pos]
        print(f"{player} Výborně!! Vyšplhej z {pos} na {new_pos}")
        pos = new_pos
    print(f"{player} je na políčku {pos}")
    return pos

def check_winner(player, pos):
    if pos == MAX_VAL:
        print(f"{player} Vyhrál!")
        sys.exit(0)

def check_same_position(player, pos, other_player, other_pos):
    if pos == other_pos:
        print(f"{player} posunul {other_player} o jedno pole zpět!")
        other_pos -= 1
        snakes, ladders = get_snakes(), get_ladders()
        if other_pos in snakes:
            new_pos = snakes[other_pos]
            print(f"{other_player} kousl had, propadáš se z {other_pos} na {new_pos}")
            other_pos = new_pos
        elif other_pos in ladders:
            new_pos = ladders[other_pos]
            print(f"{other_player} Výborně!! Vyšplhej z {other_pos} na {new_pos}")
            other_pos = new_pos
    return other_pos
