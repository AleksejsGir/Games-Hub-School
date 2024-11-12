# Проект Game Hub
#
# Вам необходимо создать консольный чат-бот Game Hub, где пользователю доступны шесть игр.
# Каждая игра располагается в отдельном модуле, которые импортируются в файл `main.py`,
# где находится меню и в котором запускается игра.
#
# main.py
import quiz_game
import rock_paper_scissors
import text_adventure
import guess_number
import hangman
import hangman_visual_effect
import minesweeper

def main():
    while True:
        print("\nДобро пожаловать в Game Hub!")
        print("1. Угадай число")
        print("2. Камень, ножницы, бумага")
        print("3. Викторина")
        print("4. Виселица")
        print("5. Виселица с визуальным эффектом")
        print("6. Текстовый квест")
        print("7. Сапер")
        print("8. Выход")
        choice = input("Выберите игру (1-7): ")
        if choice == "1":
            guess_number.guess_number()
        elif choice == "2":
            rock_paper_scissors.rock_paper_scissors()
        elif choice == "3":
            quiz_game.quiz()
        elif choice == "4":
            hangman.hangman()
        elif choice == "5":
            hangman_visual_effect.game_hangman()
        elif choice == "6":
            text_adventure.text_adventure()
        elif choice == "7":
            minesweeper.minesweeper()
        elif choice == "8":
            print("game over")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите число от 1 до 8.")

            
if __name__ == "__main__":
    main()
    print("Модуль запущен на прямую.")

        # допишите файл main.py в конце и протестируйте работоспособность всех игр.
#
# Постарайтесь реализовать не только логику игры, но и обработать потенциальный ошибочный ввод пользователя.
# Предусмотрите возможность досрочного завершения игры, возвращения в меню и выбор новой игры.
#
# Распределите создание игр между студентами своей команды. Обсуждайте возникшие трудности и делайте код ревью.
# В конце соедините получившиеся игры в файле main и протестируйте совместную работу всех игр.
#
# Обращайтесь к chatGPT только с точечными вопросами по реализации, например,
# “Как в модуле random вызвать функцию, которая выберет случайное значение в списке?”.
# Если вы обратитесь к нему с условиями игры, и он за вас ее напишет, то вы ничему не научитесь.
#
# Описания игр находятся в отдельных файлах, созданных под каждую игру.
# 1. Угадай число - guess_number.py
# 2. Камень, ножницы, бумага - rock_paper_scissors.py
# 3. Викторина - quiz_game.py
# 4. Виселица - hangman.py
# 5. Текстовый квест - text_adventure.py
# 6. Сапер - minesWeeper.py
