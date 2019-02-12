# Задача - 1 и 2.

class TownCar:
    def _init_(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        self.direction = ('налево' or 'направо')
        print('Машина повернула', direction)

class SportCar:
    def __init__ (self, speed, color, name):
        TownCar._init_ (self, speed, color, name)

class WorkCar:
    def __init__ (self, speed, color, name):
        TownCar._init_ (self, speed, color, name)

class PoliceCar:
    def __init__ (self, speed, color, name, is_police):
        TownCar._init_ (self, speed, color, name)
        self.is_police = is_police

#Вариант с super:
class Car:
    def _init_ (self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name


class NewCar:
    def _init_ (self, speed, color, name):
        super.__init__(speed, color, name)

# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

import random

class Person:
    def __init__(self, health, damage, armor, name):
        self.health = health
        self.damage = damage
        self.armor = armor
        self.name = name

    def textDescription(self):
        return 'Health: {0}. Damage: {1}. Armor: {2}. Name: {3}'.format(str(self.health), str(self.damage), str(self.armor), self.name)

enemy =  Person(10, 0, 100, 'Chell')
print(enemy.textDescription())

player = Person(10, 0, 100, 'Grimrock')
print(player.textDescription())

class Game:
    def _attackDamage(self, health, damage):
        if health[Person] < 0:
            print('Вы проиграли:-(')
        elif health [Person] - damage >= 0:
            health [Person] -= health
        return f'Нанесен урон {damage}'

    def attack(self, health, damage):
        while health[Person] > 0:
            print('Аттакуйте врага')
            if damage[enemy] > damage[player]:
                print('Chell, вы выйграли схватку')
            elif damage[player] > damage[enemy]:
                print('Grimrock, вы выйграли схватку')
            else:
                print('Поднажмите!')

    def dice(**kwargs):
        dice = [i for i in random.randint(0, 11)]
        if dice [enemy] < dice [player]:
            print(f'Ход {name}', player)
        elif dice [player] == dice [player]:
            print('Ничья! Бросьте жребий второй раз')
        else:
            print(f'Ход {name}', enemy)

# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

class Toy:
    def __init__(self, color, name, type):
        self.color = color
        self.name = name
        self.type = type

    def _tailoring(self):
        print('Пошив')

    def _coloring(self):
        print('Окраска')

    def _purchase(self):
        print('Закупка сырья')

class Cat(Toy):
    def _sound(self):
        print('Purrr...')
        
tiger = Cat('orange', 'tiger', 'cartoon')
tiger._tailoring()
tiger._sound()

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушк
