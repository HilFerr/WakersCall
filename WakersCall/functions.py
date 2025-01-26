import random, os


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def drawBoard(size):
    return [["." for _ in range(size)] for _ in range(size)]


def printBoard(board, ships = None):
    for line in board:
        for cell in line:
            if ships and cell != ".":
                ship = next((n for n in ships if n.letter == cell), None)
                if ship:
                    print(f"{ship.color}{cell}\033[0m", end=" ")
                else:
                    print(cell, end=" ")
            else:
                print(cell, end=" ")
        print()


def printShips(board, ships):
    positions = []
    for ship in ships:
        attempts = 0
        while attempts < 100:
            x, y = random.randint(0, len(board) - 1), random.randint(0, len(board) - 1)
            if board[x][y] == "." and ship.energy > 0:
                board[x][y] = ship.letter
                positions.append((x, y))
                break
            attempts += 1
        else:
            break
    return positions


def printShots(board, numOfShots, size):
    shots = []
    for _ in range(numOfShots):
        while True:
            x, y = random.randint(0, size - 1), random.randint(0, size - 1)
            if board[x][y] == ".":
                board[x][y] = "X"
                shots.append((x, y))
                break
    return shots


def updateBoard(self, board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == self.letter:
                if self.isDead:
                    board[i][j] = "."


def efficiency(totalShots, hits):
    if totalShots == 0:
        return 0
    return round((hits / totalShots) * 100, 2)
