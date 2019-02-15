#Loto

import random

class Player:
    def __init__(self, name, cards=1, points=0):
        self._cards = cards
        self._name = name
        self._points = points

    def get_points(self):
        return self._points

    def get_cards(self):
        return self._cards

    def get_name(self):
        return self._name

class Computer(Player):
    def __init__(self, points, cards, name):
        super().__init__(points, cards, name)

class User(Player):
    def __init__(self, points, cards, name):
        super().__init__(points, cards, name)

class Game:
    def __init__(self, cask, cards, computer, player):
        self._cask = cask
        self._cards = cards
        self._computer = computer
        self._player = player

    def get_cask(self):
        return self._cask

    def get_cards(self):

    def _turn(self, dice):
        dice = [i for i in random.randint(0, 11)]
        if dice[player]  > dice[computer]:
            print('Ход игрока')
        elif dice[player] < dice[computer]:
            print('Ход компьютера')
        return self._turn

cask = [i for i in range(1, 91)]
cards = cask.pop(random.randint(0, len(cask) - 1)
    def start(self):
        while len(cask) < 90:
            print(f' Номер бочонка {cards}')
            print(computer)
            print(player)
            reply = input('Зачеркнуть цифру? (y/n)')
            if reply is 'y':
                pass
            if reply is 'n':
                pass
                
player = Player('Nola', 1, 0)
computer = Computer('Robot', 1, 0)
game = Game(player, computer)
game.start()






