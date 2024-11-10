# Игра "Виселица"
import random

words = ["python", "school", "london", "barcelona", "windows"]
word = random.choice(words)
guessed_word = ['*' for _ in word]

guessed_letters = set()

def print_game():
    print("Слово:", " ".join(guessed_word))
    print("Введённые буквы:", " ".join(sorted(guessed_letters)))
    print()

def hangman():
    attempts = 6
    print(f"Оставшиеся попытки: {attempts}")
    while attempts > 0 and '*' in guessed_word:
        print_game()
        guess = input("Введите букву: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Некорректный ввод. Пожалуйста, введите одну букву.")
            continue

        if guess in guessed_letters:
            print("Вы уже вводили эту букву. Попробуйте другую.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            print(f"Отлично! Буква '{guess}' есть в слове.")
        else:
            attempts -= 1
            print(f"К сожалению, буква '{guess}' отсутствует в слове. Осталось {attempts} попыток.")

    if '*' not in guessed_word:
        print("Поздравляем! Вы угадали слово:", word)
    else:
        print("Вы проиграли! Загаданное слово было:", word)

if __name__ == "__main__":
    hangman()
    print("Модуль запущен на прямую.")


# Напишите программу для игры "Виселица". Игроку дается слово, которое он должен угадать, называя буквы.
# Если игрок называет неправильную букву, ему начисляется штрафное очко.
# Игра заканчивается победой при угадывании слова или проигрышем при достижении лимита штрафных очков.
#
# Требования:
#
# 1. Программа должна случайным образом выбирать слово из списка.
# 2. Игрок должен иметь возможность вводить буквы по одной за попытку.
# 3. Если игрок угадал букву, она должна отображаться в правильных позициях в слове.
# Вместо остальных (скрытых) букв показываются звездочки *.
# 4. Если игрок назвал неправильную букву, количество штрафных очков должно увеличиваться.
# 5. Игра заканчивается победой, если все буквы слова угаданы, или проигрышем,
# если количество штрафных очков достигает лимита (например, 6).