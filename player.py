# jmena hracu

#ansi pro cervenou, modrou. Reset davat vzdy za JMENO
def get_player_names():
    RED = "\033[91m"
    BLUE = "\033[94m"
    RESET = "\033[0m"

    player1 = input(f"{RED}Jméno 1. hráče: {RESET}").strip()
    player2 = input(f"{BLUE}Jméno 2. hráče: {RESET}").strip()

    return f"{RED}{player1}{RESET}", f"{BLUE}{player2}{RESET}"
