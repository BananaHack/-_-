from random import *

num, flag = randint(1, 100), False

while flag == False:

    the_input = int(input('Угадайте загаданное число:  '))

    if the_input < num:

        print('Слишком мало, попробуйте еще раз\n')

        continue

    elif the_input > num:

        print('Слишком много, попробуйте еще раз\n')

        continue

    elif the_input == num:

        print('Вы угадали, поздравляем!')
        repeat = input('\nВведите "Ещё", чтобы сыграть ещё раз или "Выход", чтобы закрыть игру:  ')
        while repeat != 'Ещё' or repeat != 'Выход':
            repeat = input('\nВведите "Ещё", чтобы сыграть ещё раз или "Выход", чтобы закрыть игру:  ')
            if repeat == 'Ещё':
                print()
                break
            elif repeat == 'Выход':
                #flag = True
                exit()

