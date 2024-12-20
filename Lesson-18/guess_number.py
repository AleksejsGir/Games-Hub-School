# Игра: Угадай число
#
# Используя модуль `random`, напишите программу, которая случайным образом выбирает число от 0 до 100.
# У пользователя есть 6 попыток, чтобы угадать это число. Если пользователь угадывает число,
# выводится сообщение об успехе: "Отлично! Вы угадали число … с … попытки!". Если не угадывает за 6 попыток,
# выводится сообщение о неудаче: “К сожалению, вы не угадали число. Загаданное число было: …”.
#
# В конце программы должны выводиться все попытки пользователя и загаданное число.
#
# По ходу игры после каждой попытки пользователя компьютер выводит сообщение, было ли число пользователя
# больше или меньше загаданного числа: "Загаданное число больше.", "Загаданное число меньше." соответственно.
import random



def guess_number():
    number = random.randint(1,100)
    user_trues = []
    while True:
        if len(user_trues) == 6:
            print(f'К сожалению, вы не угадали число. Загаданное число было: {number}')
            print(f'Ваши попытки: {user_trues} ')
            break
        gess = int(input('Введите число от 0 до 100: '))
        if gess >= 101:
            print(f'Число {gess} больше числа 100! Введите число от 0 до 100.')
            continue

        user_trues.append(gess)
        if gess == number:
            print(f"Отлично! Вы угадали число {number} с {len(user_trues)} попытки!")
            print(f'Ваши попытки: {user_trues} ')
            break
        elif gess < number:
            print("Загаданное число больше.")
        elif gess > number:
            print("Загаданное число меньше.")





if __name__ == "__main__":
    guess_number()
    print("Модуль запущен на прямую.")