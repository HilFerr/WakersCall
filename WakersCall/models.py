import color


class Model:
    def __init__(self, name, color, energy, letter):
        self.name = name
        self.color = color  # ANSI
        self.energy = energy
        self.letter = letter
        self.isDead = False

    def energyLoss(self, damage):
        self.energy -= damage
        if self.energy <= 0:
            self.energy = 0
            self.isDead = True

    def stats(self):
        language = ""
        if language == 'EN':
            if self.isDead:
                print(f'{self.color}{self.name} {color.WHITE}{color.NO_BOLD}{color.ITALIC} status: {color.RED}{color.NO_BOLD}{color.ITALIC}DEAD')
            else:
                print(f'{self.color}{self.name} {color.WHITE}{color.NO_BOLD}{color.ITALIC} energy: {self.energy}')
        else:
            if self.isDead:
                print(f'{self.color}{self.name} {color.WHITE}{color.NO_BOLD}{color.ITALIC} status: {color.RED}{color.NO_BOLD}{color.ITALIC}MORTO')
            else:
                print(f'{self.color}{self.name} {color.WHITE}{color.NO_BOLD}{color.ITALIC} energía: {self.energy}')
