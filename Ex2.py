# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint

def enter_data(name):
    x = int(input(f"{name}, введите количество конфет от 1 до 28, которое возьмете: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите правильное количество конфет ОТ 1 ДО 28: "))
    return x

def print_steps(name, k, counter, value):
    print(f"Ходил(а) {name}, он(она) взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

gamer1 = input("Введите имя первого игрока: ")
gamer2 = input("Введите имя второго игрока: ")
number = 2021
order = randint(0,2) 
if order:
    print(f"Первый(ая) ходит {gamer1}")
else:
    print(f"Первый(ая) ходит {gamer2}")

counter1 = 0 
counter2 = 0

while number > 28:
    if order:
        k = enter_data(gamer1)
        counter1 += k
        number -= k
        order = False
        print_steps(gamer1, k, counter1, number)
    else:
        k = enter_data(gamer2)
        counter2 += k
        number -= k
        order = True
        print_steps(gamer2, k, counter2, number)

if order:
    print(f"Выиграл(а) {gamer1} и забрал(а) все конфеты")
else:
    print(f"Выиграл(а) {gamer2} и забрал(а) все конфеты")