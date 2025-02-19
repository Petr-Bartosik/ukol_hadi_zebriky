# jmena hracu

#ansi pro cervenou, modrou. Reset davat vzdy za JMENO
def players_name():
    RED = "\033[91m" #cervena
    BLUE = "\033[94m" #modra
    RESET = "\033[0m" #na puvodni

    player1 = input(f"{RED}Jméno 1. hráče: {RESET}").strip() #strip = selekce mezer pred a za
    player2 = input(f"{BLUE}Jméno 2. hráče: {RESET}").strip()

    return f"{RED}{player1}{RESET}", f"{BLUE}{player2}{RESET}" #vraci barevna jmena
