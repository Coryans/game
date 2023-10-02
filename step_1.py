from random import randint
from random import uniform
from time import sleep
from actions import *
from data import *

# записывает игрока
name = input('Приветствую тебя в рашке! Путь тебя ждёт непростой от получения гражданства до работы на стройке! Главное не забывай платить налоги!!!. Как мне тебя называть? ')
player['name'] = name


while True:
    action = int(input(f'Выберите действие: \n1. Бой \n2. Тренировка на груше\n3. Сахарок 24 7'))
    print()
    if action == 1:
        fight()
    elif action == 2:
        train()
    elif action == 3:
        shop()    
    


