<!-- LANGUAGES -->
<div align = "center">
  <h2>LANGUAGES</h2>
  
  [![EN](https://img.shields.io/badge/EN-white.svg)](https://github.com/HilFerr/DynamicIntros/blob/main/README.md) 
  [![PT](https://img.shields.io/badge/PT-white.svg)](https://github.com/HilFerr/DynamicIntros/blob/main/README-PT.md) 
  [![ES](https://img.shields.io/badge/ES-white.svg)](https://github.com/HilFerr/DynamicIntros/blob/main/README-ES.md)  
</div>

<!-- IMAGE -->
<div align = "center">
  <img src="img/logo.png" width="250px">
</div>

<!-- INTRO -->
<div align = "center">
  <h1>WAKER'S CALL</h1>
  <h3>PYTHON GAME</h3>

  <strong>Waker's Call</strong> is the name of a game where the user must hit all the ships on a board.
  
  This was built with

  ![PYTHON](https://img.shields.io/badge/python-white.svg?style=for-the-badge&logo=python&logoColor=0d1117)
</div>

<br>

<!-- EXPLANATION -->
<div align = "center">
  <h1>EXPLANATION</h1>


  <!-- MAIN.PY -->
  <details>
  <summary><h2>MAIN.PY</h2></summary>
  <br>
    
  **Document that is used to execute both versions of the game. As well as to give the user the language choice.**
  
  <br>
  
  <div align = "left">

  <div align = "center"><h3>LANGUAGE()</h3></div>

  <br>
  
  ```
  def language():
    language = ""

    while language not in ['EN', 'PT']:
        language = input(color.WHITE + color.BOLD + color.NO_ITALIC + 'Choose a language [EN | PT]: ').strip().upper()

        if language not in ['EN', 'PT']:
            print(color.RED + color.NO_BOLD + color.ITALIC + 'Invalid language.')
            input('Press [ENTER] to retry.')
        cls()
    return language
  ```

  This prompt is used for the user to choose the UI language of the game. The user must choose either English or Portuguese, if none is selected they must try again.

  The chosen language is then saved in the function itself, later to be used throughout the game.
  
  <br>
  <br>
  
  ```
  if __name__ == "__main__":
      language = language()
  
      if language == 'EN':
          gameEN.main()
      else:
          gamePT.main()   
  ```

  Depending on the language given by the function, this will run a different document (gameEN.py or gamePT.py).

  </div>

  </details>











  <!-- GAMEEN.PY & GAMEPT.PY -->
  <details>
  <summary><h2>GAME.PY</h2></summary>
  <br>
    
  **Document that connects every created function and uses them for their intended purpose.**
  
  <br>
  
  <div align = "left">

  <div align = "center"><h3>COVER() FUNCTION</h3></div>

  <br>
  
  ```
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
  ```

  Prints directly after the language prompt.
  
  <br>
  <br>

  <div align = "center"><h3>MAIN() FUNCTION</h3></div>

  <br>

  At this point the ***main()*** function starts, so I'll cut it in multiple snippets for a better understanding.
  
  ```
  def main():
      cover()
  
      ship1 = Model("Explorer", color.BLUE + color.BOLD + color.NO_ITALIC, 30, "E")
      ship2 = Model("Defender", color.GREEN + color.BOLD + color.NO_ITALIC, 25, "D")
      ship3 = Model("Attacker", color.RED + color.BOLD + color.NO_ITALIC, 20, "A")
      ships = [ship1, ship2, ship3]
  
      boardSize = 5
      totalShots = 0
      hits = 0
  ```

  In the beginning, the function *cover()* is called.

  After that, the **ships are defined**. Giving them their own, individual colors, styles, energy points and a letter to be used in the board.

  Under it, the board size value is set. The total number of shots fired is set to 0 and so is the total number of hits.

  <br>

  > <h3>NOTE</h3>
  > 
  > You can change this value to any value. **Caution**, as it will change the number of columns and rows, disrupting the already balanced game.
  > 
  > ```
  > boardSize = 5
  > ```

  <br>
  <br>

  <div align = "center"><h3>MAIN GAME LOOP</h3></div>

  <br>

  ```
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
  ```

  **The loop repeats itself every round, updating the data inside the variables.**
  
  It starts by clearing the screen, with the function *cls()*.
  
  After that, it prints both the **ship's board** and the **game board** (the board where the shots will be printed). Then, the **stats** are printed, showing the number of shots shot, the number of hits, and the accuracy percentage.

  <br>
  <br>
  
  ```
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
  ```

  This snippet handles the logic of hitting ships, their reduction of energy, and their destruction.
  
  Giving it a closer inspection:

  > **1st line:** Cycles through every shot shot.
  > 
  > **2nd line:** Checks if a shot landed in a position of a ship.
  > 
  > **3rd line:** Adds 1 value to the hit counter.
  > 
  > **4th - 6th line:** Searches for a hit ship and reduces 10 energy from it.
  > 
  > **7th - 10th line:** If the energy of a ship is 0, it is deleted.
  >
  > **12th line:** Add 3 shots to the total shots counter.

  <br>
  <br>

  ```
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
  ```

  **Code only executed if every ship's energy is set to 0 or if the total shots count reaches 105.**

  It prints the stats of the game. The amount of shots shot, the amount of hits, and the accuracy.

  The last line repeats the loop, all over again.

  <br>
  <br>

  ```
  if __name__ == "__main__":
    main()
  ```

  Both the main game loop and the main() function end here. But this snippet is the one that executes the program.

  <br>

  > <h3>NOTE</h3>
  > 
  > The Portuguese version of the game is the same, just with the UI elements translated to the language.

  </div>

  </details>










  <!-- FUNCTIONS.PY -->
  <details>
  <summary><h2>FUNCTIONS.PY</h2></summary>
  <br>
    
  **Document that houses all game functions.**
  
  <br>
  
  <div align = "left">

  For these functions to work, the following libraries are needed.

  ```
  import random
  import os
  ```

  <div align = "center"><h3>CLS()</h3></div>

  <br>
  
  ```
  def cls():
      os.system("cls" if os.name == "nt" else "clear")
  ```

  Method used to clear the terminal.
  
  <br>
  <br>
  
  <div align = "center"><h3>DRAWBOARD()</h3></div>

  <br>
  
  ```
  def drawBoard(size):
      return [["." for _ in range(size)] for _ in range(size)]
  ```

  Method used to clear the terminal.
  
  <br>
  <br>
  
  <div align = "center"><h3>PRINTBOARD()</h3></div>

  <br>
  
  ```
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
  ```

  Method that prints a board with nothing.
  
  <br>
  <br>
  
  <div align = "center"><h3>PRINTSHIPS()</h3></div>

  <br>
  
  ```
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
  ```

  Method that adds ships onto random locations inside the first board.
  
  <br>
  <br>
  
  <div align = "center"><h3>PRINTSHOTS()</h3></div>

  <br>
  
  ```
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
  ```

  Method that adds shots onto random locations inside the second board.
  
  <br>
  <br>
  
  <div align = "center"><h3>UPDATEBOARD()</h3></div>

  <br>
  
  ```
  def updateBoard(self, board):
      for i in range(len(board)):
          for j in range(len(board[i])):
              if board[i][j] == self.letter:
                  if self.isDead:
                      board[i][j] = "."
  ```

  Method ensures that all the ships tagged with the var *isDead* are deleted from the board.
  
  <br>
  <br>
  
  <div align = "center"><h3>EFFICIENCY()</h3></div>

  <br>
  
  ```
  def efficiency(totalShots, hits):
      if totalShots == 0:
          return 0
      return round((hits / totalShots) * 100, 2)
  ```

  Calculates the average of shots that are a hit.
  
  <br>
  <br>
  
  </div>

  </details>










  <!-- MODELS.PY -->
  <details>
  <summary><h2>MODELS.PY</h2></summary>
  <br>
    
  **Document that stores information about the ships and the template for the stats.**
  
  <br>
  
  <div align = "left">

  Every piece of code is inside of the ***Class Model***.
  
  ```
  class Model:
      def __init__(self, name, color, energy, letter):
          self.name = name
          self.color = color  # ANSI
          self.energy = energy
          self.letter = letter
          self.isDead = False
  ```

  The first method, shown above, stores the information about each ship.
  
  <br>
  <br>
  
  ```
    def energyLoss(self, damage):
        self.energy -= damage
        if self.energy <= 0:
            self.energy = 0
            self.isDead = True
  ```

  The second method, still inside of the *class Model*, determines what happens when a ship gets hit by a shot.
      
  <br>
  <br>
  
  ```
    def energyLoss(self, damage):
        self.energy -= damage
        if self.energy <= 0:
            self.energy = 0
            self.isDead = True
  ```

  The third and last method determines how each ship's stats should appear, whether the ship is alive or dead.
  
  </div>

  </details>









  
  <!-- COLORS.PY -->
  <details>
  <summary><h2>COLORS.PY</h2></summary>
  <br>
    
  **Document just stores color presets.**
  
  <br>
  
  <div align = "left">
  
  ```
  RED       = '\033[31m'
  GREEN     = '\033[32m'
  YELLOW    = '\033[33m'
  BLUE      = '\033[34m'
  WHITE     = '\033[37m'
  
  ITALIC    = '\033[3m'
  NO_ITALIC = '\033[23m'
  
  BOLD      = '\033[1;1m'
  NO_BOLD   = '\033[22m'
  ```

  </div>

  </details>
</div>

<br>
<div align = "center">
  <h1>HOW TO RUN IT</h1>

  Download the files or copy them into your project.
</div>
