import sys
from game_board import get_snakes, get_ladders

MAX_VAL = 100 #maximalni hodnota herni desky

#posun o hozeny pocet + aplikace pravidel - hadi, zebriky, posledni pole limit max
def move_player(player, pos, dice_val):
    old_pos = pos
    pos += dice_val #stavajici pozice + pricteni hozene hodnoty

    if pos > MAX_VAL:
        print(f"{player} potřebuje {MAX_VAL - old_pos} k vítězství. Zkus to znova.")
        return old_pos #prehodi max val = zustava

    #______________nacteni hadu a zebriku________________________________________________________________
    snakes, ladders = get_snakes(), get_ladders() #nacteni hadu a zebriku

    #_____________ aplikace hada_______________________________________________________________________________________
    if pos in snakes:
        new_pos = snakes[pos]
        print(f"{player} kousl had, propadáš se z {pos} na {new_pos}")
        pos = new_pos

    #______________aplikace zebriku____________________________________________________________________________________
    elif pos in ladders:
        new_pos = ladders[pos]
        print(f"{player} Výborně!! Vyšplhej z {pos} na {new_pos}")
        pos = new_pos
    print(f"{player} je na políčku {pos}")
    return pos

def check_winner(player, pos): #kontrola výhry
    if pos == MAX_VAL: #jestliže dosáhne max vall/100/
        print(f"{player} Vyhrál! Za odměnu můžeš hrát znova.")
        sys.exit(0) #ukonceni programu

        #_______________#kontrola pozice a pokud je na policku jiz hrac, vrati jej o pole zpet___________________________
def check_same_position(player, pos, other_player, other_pos):
    if pos == other_pos:
        print(f"{player} posunul {other_player} o jedno pole zpět!")
        other_pos -= 1 #posun o jedno zpet

        snakes, ladders = get_snakes(), get_ladders()#nacteni hadu a zebriku
        #_______________kontrola jeslti stoupl na zebrik nebo hada_____________________________________________________
        if other_pos in snakes:
            new_pos = snakes[other_pos]
            print(f"{other_player} kousl had, propadáš se z {other_pos} na {new_pos}")
            other_pos = new_pos #posun dolů
        elif other_pos in ladders:
            new_pos = ladders[other_pos]
            print(f"{other_player} Výborně!! Vyšplhej z {other_pos} na {new_pos}")
            other_pos = new_pos #posun nahoru

    return other_pos #vraceni upravene pozice
