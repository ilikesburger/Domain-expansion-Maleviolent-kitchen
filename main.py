class Player:
    def __int__(self, power, agility, accuracy, stamina):
        self.power = power
        self.agility = agility
        self.accuracy = accuracy
        self.stamina = stamina


class Goalkeeper(Player):
    def __init__(self, power, speed, accuracy, stamina):
        super().  __init__ (power, speed, accuracy, stamina)

    def save(self):
        print('Поймал мяч')


