from random import *

flag = 'да'


def right_now():
    global a
    for i in range(8):
        print(end="\n")
        for j in range(8):
            print(a[i][j], end=" ")
    print(end='\n')
    print()


def kill(vh, n):
    if vh == 'в':
        for i in range(8):
            a[i][n - 1] = 0
    if vh == 'г':
        for i in range(8):
            a[n - 1][i] = 0


print()
print('Приветствую тебя в суперниме!')
print()

while flag == 'да' or flag == 'Да':
    bot_or_real = input('Если Вы хотите поиграть с ботом, то напишите слово "бот", если же с реальным игроком, то слово "игрок": ')
    a = [[0] * 8 for i in range(8)]
    for s in range(8):
        for z in range(8):
            a[s][z] = randint(0, 1)
    if bot_or_real == 'игрок':
        p = 2
        w = 0
        right_now()
        while w != 64: 
            if p == 1:
                p = 2
            else:
                p = 1
            if p == 1:
                print('Ход 1 игрока:')
                print()
            else:
                print('Ход 2 игрока:')
                print()
            vh, n = input('Введите вертикаль (в) / горизонталь (г): '), int(input('Введите номер горизонтали / вертикали: '))
            kill(vh, n)
            w = 0
            for i in range(8):
                for j in range(8):
                    if a[i][j] == 0:
                        w += 1
            right_now()
    else:
        p = 2
        w = 0
        right_now()
        while w != 64: 
            if p == 1:
                p = 2
            else:
                p = 1
            if p == 1:
                print('Ход бота (игрока 1):')
                print()
                pre_vh = randint(0, 1)
                if pre_vh == 0:
                    vh = 'г'
                else:
                    vh = 'в'
                status = 0
                if pre_vh == 0:
                    status = 0
                    while status == 0:
                        n = randint(1, 8)
                        for i in range(8):
                            for j in range(8):
                                if a[n - 1][j] == 1:
                                    status +=  1
                    print('Бот убрал горизонталь ' + str(n))
                else:
                    while status == 0:
                        n = randint(1, 8)
                        for i in range(8):
                            for j in range(8):
                                if a[i][n - 1] == 1:
                                    status +=  1
                    print('Бот убрал вертикаль ' + str(n))
                kill(vh, n)
                w = 0
                for i in range(8):
                    for j in range(8):
                        if a[i][j] == 0:
                            w += 1
            else:
                print('Ход игрока 2:')
                print()
                vh, n = input('Введите вертикаль (в) / горизонталь (г): '), int(input('Введите номер горизонтали / вертикали: '))
                kill(vh, n)
                w = 0
                for i in range(8):
                    for j in range(8):
                        if a[i][j] == 0:
                            w += 1
            right_now()
    print('Победил игрок ', p)
    flag = input('Вы хотите продолжить игру? ')
