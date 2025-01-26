import color
import gameEN, gamePT
from functions import cls


cls()

def language():
    language = ""

    while language not in ['EN', 'PT']:
        language = input(color.WHITE + color.BOLD + color.NO_ITALIC + 'Choose a language [EN | PT]: ').strip().upper()

        if language not in ['EN', 'PT']:
            print(color.RED + color.NO_BOLD + color.ITALIC + 'Invalid language.')
            input('Press [ENTER] to retry.')
        cls()
    return language


if __name__ == "__main__":
    language = language()

    if language == 'EN':
        gameEN.main()
    else:
        gamePT.main()   
