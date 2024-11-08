# Игра: Камень, ножницы, бумага
#
# Создайте игру "Камень, ножницы, бумага", где пользователь играет против компьютера.
# Компьютер случайным образом выбирает одно из трех значений: камень, ножницы или бумагу.
# Пользователь вводит свой выбор, и программа определяет победителя. Если выборы одинаковы, игра объявляет ничью.
# Игра продолжается до тех пор, пока один из игроков (пользователь или компьютер)
# не одержит на три победы больше, чем соперник. В конце показывается итоговый счет и объясляется победитель.
# Игра: Камень, ножницы, бумага
#
# Создайте игру "Камень, ножницы, бумага", где пользователь играет против компьютера.
# Компьютер случайным образом выбирает одно из трех значений: камень, ножницы или бумагу.
# Пользователь вводит свой выбор, и программа определяет победителя. Если выборы одинаковы, игра объявляет ничью.
# Игра продолжается до тех пор, пока один из игроков (пользователь или компьютер)
# не одержит на три победы больше, чем соперник. В конце показывается итоговый счет и объясляется победитель.


import random

winnings_score = 3
def rock_paper_scissors():
    player_trys = 0
    comp_trys = 0
    while player_trys < winnings_score and comp_trys < winnings_score:
        player_choice= input("Сделайте ваш выбор: камень, ножницы, бумага: ")
        computer_choice = get_computer_choice()
        print(f'Компьютер выбрал: {computer_choice}')

        winner = get_winner(player_choice, computer_choice)
        if winner == "Игрок":
            player_trys +=1
            print("Вы победили в этом раунде")
        elif winner == "Компьютер":
            comp_trys += 1
            print("Компьютер победил в этом раунде")
        else:
            print("Ничья")
        print(f"Счет - Игрок : {player_trys},Компьютер: {comp_trys}" )
    if player_trys == winnings_score:
        print("Поздравляем!Вы выиграли игру!!!")
    else:
        print("Компьютер выиграл игру!.Попробуйте снова!!")

def get_computer_choice():
    return random.choice(["камень", "ножницы", "бумага"])

def get_winner(player, computer):
    if player == computer :
        return "Ничья"
    elif (player == "камень" and computer == "ножницы" ) or \
         (player == "ножницы" and computer == "бумага") or \
         (player == "бумага" and computer == "камень") :
        return "Игрок"
    else:
        return "Компьютер"


if __name__ == "__main__":
    rock_paper_scissors()
    print("Модуль запущен на прямую.")

#         possible_actions = ["камень", "ножницы", "бумага"]
#         comp = random.choice(possible_actions)
#         print(f"\nВы выбрали {player}, соперник выбрал {comp}.\n")
#         if player == comp:
#             print(f"Ничья.Счет:{player_trys}:{comp_trys}")
#         elif player == "камень":
#             if  comp == "ножницы":
#                 player_trys += 1
#             print(f'Вы выиграли.Счет:{player_trys}:{comp_trys}')
#             else:
#             comp_trys += 1
#             print(f"Вы проиграли.Счет:{player_trys}:{comp_trys}")
#             elif player == "бумага":
#             if comp == "камень":
#                 player_trys += 1
#                 print(f"Вы выиграли.Счет:{player_trys}:{comp_trys}")
#                 else:
#                 comp_trys += 1
#                 print(f"Вы проиграли.Счет:{player_trys}:{comp_trys}")
#                 elif player == "ножницы":
#                 if comp == "бумага":
#                     player_trys += 1
#                     print(f"Вы выиграли.Счет:{player_trys}:{comp_trys}")
#                     else:
#                     comp_trys += 1
#                     print(f"Вы проиграли.Счет:{player_trys}:{comp_trys}")
# if player_trys == winnings_score:
#     print(f"Вы выиграли игру.Счет:{player_trys}:{comp_trys}")
#     else:
#     comp_trys == winnings_score
#     print(f"Компьютер выиграл игру.Счет:{player_trys}:{comp_trys}")
#
#
#
# rock_paper_scissors()
