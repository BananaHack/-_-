from random import *

def number():
    num = randint(1, 100)
    return num

random_number = number()

while True:
    user_input = int(input('Угадайте загаданное число:  '))

    if user_input < random_number:
        print('Слишком мало, попробуйте еще раз\n')
        continue

    elif user_input > random_number:
        print('Слишком много, попробуйте еще раз\n')
        continue

    elif user_input == random_number:
        print('Вы угадали, поздравляем!')
        while True:
            repeat = input('\nВведите "Ещё", чтобы сыграть ещё раз или "Выход", чтобы закрыть игру:  ')
            if repeat == 'Ещё':
                print()
                break

            elif repeat == 'Выход':
                exit()
                
        random_number = number()
        continue
