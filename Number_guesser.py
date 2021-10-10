from random import randint
from time import sleep
from os import system, name

# генерация искомого случайного числа
def number():
    num = randint(1, 100)
    return num

# проверка корректности пользовательского ввода
def is_valid(user_input):
    if user_input.isdigit() and 1 <= int(user_input) <= 100:
        user_input = int(user_input)
        return user_input
    else:
        return False

# очистка консоли для новой игры
def cls():
    system('cls' if name=='nt' else 'clear')
        

random_number, counter, best_score = number(), 1, 9999
one_more_time = ['Ещё', 'Еще', 'ещё', 'еще', 'ЕЩЁ', 'ЕЩЕ', 'ЕЩё', 'ЕЩе', 'еЩЁ', 'еЩЕ', 'To~', 'Tot', 'TOT', 'tot', 'TO`', 'TOt', 'tO`', 'tOT']
the_exit = ['Выход', 'ВЫход', 'выход', 'ВЫХОД', 'Ds[jl', 'DS[jl', 'ds[jl', 'DS[JL']
print('Добро пожаловать в числовую угадайку!\n')
sleep(2)

while True:

    print('Попытка №', counter)
    user_input = input('Угадайте загаданное число:  ')
    if is_valid(user_input) == False:
        print('Пожалуйста, введите целое число от 1 до 100\n\n')
        sleep(2)
        continue

       
    if is_valid(user_input) < random_number:
        print('Слишком мало, попробуйте еще раз\n')
        counter += 1
        continue

    elif is_valid(user_input) > random_number:
        print('Слишком много, попробуйте еще раз\n')
        counter += 1
        continue

    elif is_valid(user_input) == random_number:
        if counter < best_score:
            best_score = counter
        print('\nВы угадали, поздравляем!\nБыло потрачено', counter, 'попыток.\tРекорд:', best_score, 'попыток')
        while True:
            repeat = input('\nВведите "Ещё", чтобы сыграть ещё раз или "Выход", чтобы закрыть игру:  ')
            if repeat in one_more_time:
                print()
                break

            elif repeat in the_exit:
                exit()
                
                
        random_number = number()
        counter = 1
        cls()
        print('Игра "Числовая угадайка"\n')
        continue
