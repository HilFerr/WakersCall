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
    input("Press [ENTER] to start...")


def main():
    cover()

    ship1 = Model("Explorer", color.BLUE + color.BOLD + color.NO_ITALIC, 30, "E")
    ship2 = Model("Defender", color.GREEN + color.BOLD + color.NO_ITALIC, 25, "D")
    ship3 = Model("Attacker", color.RED + color.BOLD + color.NO_ITALIC, 20, "A")
    ships = [ship1, ship2, ship3]

    boardSize = 5
    totalShots = 0
    hits = 0


    while True:
        cls()

        shipsBoard = drawBoard(boardSize)
        shotsBoard = drawBoard(boardSize)

        shipsPositions = printShips(shipsBoard, ships)
        shots = printShots(shotsBoard, 3, boardSize)

        print(color.WHITE + color.BOLD + color.NO_ITALIC + "\nSHIP'S BOARD:")
        printBoard(shipsBoard, ships)

        print(color.WHITE + color.BOLD + color.NO_ITALIC + "\nGAME BOARD:")
        printBoard(shotsBoard, ships)

        print(color.WHITE + color.BOLD + color.NO_ITALIC + "\nSTATS:")
        for ship in ships:
            ship.stats()

        print(color.YELLOW + color.BOLD + color.NO_ITALIC + "\nTotal Shots:", color.WHITE + color.NO_BOLD + color.ITALIC, totalShots)
        print(color.YELLOW + color.BOLD + color.NO_ITALIC + "Hits:", color.WHITE + color.NO_BOLD + color.ITALIC, hits)
        print(color.YELLOW + color.BOLD + color.NO_ITALIC + "Accuracy:", color.WHITE + color.NO_BOLD + color.ITALIC, efficiency(totalShots, hits), "%")


        for shot in shots:
            if shot in shipsPositions:
                hits += 1
                for ship in ships:
                    if shipsBoard[shot[0]][shot[1]] == ship.letter:
                        ship.energyLoss(10)
                        if ship.energy == 0:
                            shipsBoard[shot[0]][shot[1]] = "."
                            cls()
                            print(color.RED + color.BOLD + color.NO_ITALIC + f"\n{ship.name} has been destroyed!")

        totalShots += 3     


        if all(ship.energy == 0 for ship in ships) or totalShots >= 105:
            cls()
            print(color.RED + color.BOLD + color.NO_ITALIC + ("\n=== GAME OVER ===\n"))

            for ship in ships:
                ship.stats()

            print(color.YELLOW + color.NO_BOLD + color.NO_ITALIC + "\nTotal Shots:", 
                  color.WHITE + color.NO_BOLD + color.ITALIC, totalShots, 
                  color.YELLOW + color.NO_BOLD + color.NO_ITALIC + " Accurate Shots:",
                  color.WHITE + color.NO_BOLD + color.ITALIC, hits)
            print(color.YELLOW + color.NO_BOLD + color.NO_ITALIC + "Final Accuracy:", color.WHITE + color.NO_BOLD + color.ITALIC, efficiency(totalShots, hits), "% \n")
            break

        input(color.RED + color.NO_BOLD + color.ITALIC + ("\nPress [ENTER] for the next round..."))


if __name__ == "__main__":
    main()
