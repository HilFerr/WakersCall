import color
from models import *
from functions import *


def cover():
    print("""
          
    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓███████▓▒░       ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░        
    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░ ░▒▓██████▓▒░       ░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
    ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░        
     ░▒▓█████████████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░        ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓████████▓▒░ 
    
    """)
    input("Pressione o [ENTER] para começar...")


def main():
    cover()

    ship1 = Model("Explorador", color.BLUE + color.BOLD + color.NO_ITALIC, 30, "E")
    ship2 = Model("Defensor", color.GREEN + color.BOLD + color.NO_ITALIC, 25, "D")
    ship3 = Model("Atacante", color.RED + color.BOLD + color.NO_ITALIC, 20, "A")
    ships = [ship1, ship2, ship3]

    board_size = 5
    total_shots = 0
    hits = 0


    while True:
        cls()

        ships_board = drawBoard(board_size)
        shots_board = drawBoard(board_size)

        ships_positions = printShips(ships_board, ships)
        shots = printShots(shots_board, 3, board_size)

        print(color.WHITE + color.BOLD + color.NO_ITALIC + "\nTABULEIRO DAS NAVES:")
        printBoard(ships_board, ships)

        print(color.WHITE + color.BOLD + color.NO_ITALIC + "\nTABULEIRO DE JOGO:")
        printBoard(shots_board, ships)

        print(color.WHITE + color.BOLD + color.NO_ITALIC + "\nESTATÍSTICAS:")
        for ship in ships:
            ship.stats()

        print(color.YELLOW + color.BOLD + color.NO_ITALIC + "\nTotal de Tiros:", color.WHITE + color.NO_BOLD + color.ITALIC, total_shots)
        print(color.YELLOW + color.BOLD + color.NO_ITALIC + "Acertos:", color.WHITE + color.NO_BOLD + color.ITALIC, hits)
        print(color.YELLOW + color.BOLD + color.NO_ITALIC + "Eficâcia:", color.WHITE + color.NO_BOLD + color.ITALIC, efficiency(total_shots, hits), "%")


        for shot in shots:
            if shot in ships_positions:
                hits += 1
                for ship in ships:
                    if ships_board[shot[0]][shot[1]] == ship.letter:
                        ship.energyLoss(10)
                        if ship.energy == 0:
                            ships_board[shot[0]][shot[1]] = "."
                            cls()
                            print(color.RED + color.BOLD + color.NO_ITALIC + f"\n{ship.name} foi destruída!")

        total_shots += 3


        if all(ship.energy == 0 for ship in ships) or total_shots >= 105:
            cls()
            print(color.RED + color.BOLD + color.NO_ITALIC + ("\n=== FIM DO JOGO ===\n"))

            for ship in ships:
                ship.stats()

            print(color.YELLOW + color.NO_BOLD + color.NO_ITALIC + "\nTotal de Tiros:", 
                  color.WHITE + color.NO_BOLD + color.ITALIC, total_shots, 
                  color.YELLOW + color.NO_BOLD + color.NO_ITALIC + " Acertos:",
                  color.WHITE + color.NO_BOLD + color.ITALIC, hits)
            print(color.YELLOW + color.NO_BOLD + color.NO_ITALIC + "Eficâcia Final:", color.WHITE + color.NO_BOLD + color.ITALIC, efficiency(total_shots, hits), "% \n")
            break

        input(color.RED + color.NO_BOLD + color.ITALIC + ("\nPressione o [ENTER] para a próxima ronda..."))


if __name__ == "__main__":
    main()
