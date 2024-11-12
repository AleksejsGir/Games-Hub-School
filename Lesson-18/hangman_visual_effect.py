# Игра "Виселица"
#
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

import random
#список слов

import random

def display_game_state(word, guessed_letters): #добавил аргументы (word, guessed_letters)
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "*"
    print(display_word)

def process_letter(word, letter, guessed_letters, wrong_attempts): #добавил аргументы (word, letter, guessed_letters, wrong_attempts)
    if letter in word:
        guessed_letters.append(letter)
    else:
        wrong_attempts += 1
    return wrong_attempts

def display_hangman(attempts):
    stages = [
        """
           --------
           |      |
           |      
           |    
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |     
        --------
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |     
        --------
        """
    ]
    return stages[attempts]

def game_hangman():
    words = ["mouse", "elephant", "duck", "cat", "dog", "horse"]
    word = random.choice(words)
    guessed_letters = []
    wrong_attempts = 0
    max_attempts = 6

    while wrong_attempts < max_attempts:
        print(display_hangman(wrong_attempts))
        display_game_state(word, guessed_letters)
        letter = input("Введите букву: ")
        if letter in guessed_letters:
            print("Вы уже угадали эту букву.")
            continue
        wrong_attempts = process_letter(word, letter, guessed_letters, wrong_attempts) # добавил переменную wrong_attempts
        if all(letter in guessed_letters for letter in word):
            print(f"Поздравляем, вы выиграли! Загаданное слово: {word}")
            break
    else:
        print(display_hangman(wrong_attempts))
        print(f"Вы проиграли! Загаданное слово было: {word}")

if __name__ == "__main__":
    game_hangman()
