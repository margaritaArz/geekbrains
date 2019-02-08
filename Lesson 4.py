#Easy: Задание-1:

list = [i for i in range (10)]


list1 = [i**2 for i in list]

print(list, list1)

# Задание-2:

fruit1 = ['яблоко', 'мандарин', 'груша', 'манго']
fruit2 = ['апельсин', 'груша', 'киви', 'яблоко', 'банан']
new_list = []

for i1 in fruit1:
    for i2 in fruit2:
        if i1 == i2:
           new_list.append(i1)

print(new_list)

# Задание-3:

import random

numberList = []

for _ in range(10):
    numberList.append(random.randint(-10, 10))

numberList1 = [el for el in numberList if el >= 0 and el % 3 == 0 and el % 4 != 0]

print(numberList, 'новый спискок =', numberList1)

# Normal: Задача - 1

name = input('Name: ')
surname = input('Surname ')
email = input('Your email ')

import re

patternEmail = '[a-z0-9_]+@[a-z0-9]+\.(com|org|ru)'
print(re.match(patternEmail, email))

pattern1 = '^[A-Z]{1,1}'
print(re.match(pattern1, surname))
print(re.match(pattern1, name))

# Задача - 2:

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

regularExp = '\...{3}'

if re.search(regularExp, some_str) is None:
    print('В тексте нет более одной точки подряд')
else:
    print('В тексте найдено несколько точек подряд')

# Hard, Задание:

person1 = {'card': 4276123465440000, 'pin': 9090, 'money': 100.90}
person2 = {'card': 4276123465440001, 'pin': 9091, 'money': 200.90}
person3 = {'card': 4276123465440002, 'pin': 9092, 'money': 300.90}

bank = [person1, person2, person3]


def get_person_by_card(card_number):
    for person in bank:
        if person['card'] == card_number:
            return person


def is_pin_valid(person, pin_code):
    if person['pin'] == pin_code:
        return True
    return False


def check_account(person):
    return round(person['money'], 2)


def withdraw_money(person, money):
    if person['money'] - money >= 0:
        person['money'] -= money
        return 'Вы сняли {} рублей.'.format(money)
    elif person['money'] < money:
        return 'На вашем счету недостаточно средств!'


def process_user_choice(choice, person):
    if choice == 1:
        print('Ваш баланс:', check_account(person))
    elif choice == 2:
        count = float(input('Сумма к снятию: '))
        print(withdraw_money(person, count))


def start():
    try:
        card_number, pin_code = input('Введите номер карты и пин код через пробел: ').split()
        card_number = int(card_number)
        pin_code = int(pin_code)
        person = get_person_by_card(card_number)

    except ValueError:
        print('Вы должны ввести цифры. Через пробел')

    try:
        if person and is_pin_valid(person, pin_code):
            while True:
                choice = int(input('Выберите пункт:\n'
                               '1. Проверить баланс\n'
                               '2. Снять деньги\n'
                               '3. Выход\n'
                               '---------------------\n'
                               'Ваш выбор: '))

                if choice == 3:
                    break
                process_user_choice(choice, person)
        else:
            print('Номер карты или пин код введены не верно!')

    except ValueError:
        print('Вы должны ввести цифры ')

start()