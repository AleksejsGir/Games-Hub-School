# Игра "Текстовый квест"
#
# Напишите программу для текстовой игры-квеста. Игроку предлагается сюжетная история с различными вариантами действий.
# В зависимости от выбора игрока, история развивается по-разному.
# Цель — пройти игру, приняв правильные решения и достигнув конца истории.
#
# Требования:
#
# 1. Программа должна предлагать игроку несколько вариантов действий в каждом шаге истории.
# 2. Игрок должен вводить свой выбор, который влияет на дальнейшее развитие сюжета.
# 3. Игра должна иметь несколько концовок в зависимости от выбора игрока.
# 4. Программа должна корректно обрабатывать ввод пользователя и предоставлять соответствующую обратную связь.
#
# Сюжет игры:
# Игрок оказывается в загадочном замке и должен пройти через несколько комнат, делая выборы,
# которые повлияют на развитие сюжета и конечный исход. Цель — найти выход из замка, избегая опасностей и решая загадки.
#
# Сюжет:
#
# 1. Начало приключения:
# Вы просыпаетесь в темной комнате замка. Перед вами две двери: левая и правая.
#     - Выбор:
#         - Левая дверь
#         - Правая дверь
# 2. Левая дверь:
# Вы входите в левую комнату и видите старинный сундук.
#     - Выбор:
#         - Открыть сундук
#         - Не открывать сундук и выйти
# 3. Открыть сундук:
# В сундуке оказывается карта с указанием выхода из замка.
#     - Выбор:
#         - Следовать по карте
#         - Игнорировать карту и исследовать комнату
# 4. Следовать по карте:
# Вы идете по карте и приходите к тайному проходу.
#     - Выбор:
#         - Войти в проход
#         - Оставить проход и вернуться назад
# 5. Войти в проход:
# Проход приводит вас к выходу из замка. Вы выиграли!
# 6. Не открывать сундук и выйти:
# Вы выходите из комнаты и попадаете в коридор с двумя новыми дверями.
#     - Выбор:
#         - Первая дверь
#         - Вторая дверь
# 7. Первая дверь:
# Вы входите в первую дверь и видите старого мага.
#     - Выбор:
#         - Поговорить с магом
#         - Игнорировать мага и выйти
# 8. Поговорить с магом:
# Маг дает вам волшебный ключ, который открывает все двери в замке.
#     - Выбор:
#         - Использовать ключ для выхода
#         - Оставить ключ и искать дальше
# 9. Использовать ключ для выхода:
# Вы находите дверь, открываете ее ключом и выходите из замка. Вы выиграли!
# 10. Правая дверь:
# Вы входите в правую комнату и видите лестницу, ведущую вниз.
#     - Выбор:
#         - Спуститься по лестнице
#         - Остаться наверху
# 11. Спуститься по лестнице:
# Лестница ведет вас в подземелье, где вас поджидает дракон.
#     - Выбор:
#         - Сражаться с драконом
#         - Бежать от дракона
# 12. Сражаться с драконом:
# Вы сражаетесь храбро, но дракон оказывается слишком сильным. Вы проиграли.
# 13. Бежать от дракона:
# Вы бежите обратно по лестнице, но дверь наверху оказывается заперта. Вы в ловушке. Вы проиграли.
# 14. Остаться наверху:
# Вы решаете не спускаться по лестнице и находите потайную дверь за картиной.
#     - Выбор:
#         - Войти в потайную дверь
#         - Игнорировать дверь и вернуться назад
# 15. Войти в потайную дверь:
# Потайная дверь приводит вас к выходу из замка. Вы выиграли!
# 16. Вторая дверь:
# Вы входите во вторую дверь и видите зеркало, в котором отражается другая комната.
#     - Выбор:
#         - Войти в зеркало
#         - Разбить зеркало
# 17. Войти в зеркало:
# Вы проходите через зеркало и оказываетесь в другой части замка, где находите выход. Вы выиграли!
# 18. Разбить зеркало:
# Зеркало разбивается, и вы оказываетесь в ловушке. Вы проиграли.
def text_adventure():
    print("Начало приключения:")
    print("Вы просыпаетесь в темной комнате замка. Перед вами две двери: левая и правая.")
    select_dour = input("Введите 1, если левая дверь или 2 если правая дверь: ")
    if select_dour == "1":
        print("Вы входите в левую комнату и видите старинный сундук.")
    else:
        print("Вы входите в правую комнату и видите лестницу, ведущую вниз.")
        choice_x = input("Выбор: 1 - спуститься по лестнице, 2 - остаться на верху. ")
        if choice_x == "1":
            print("Лестница ведет вас в подземелье, где вас поджидает дракон.")
            choice_x_1 = input("Выбор: 1 - сражаться с драконом, 2 - бежать от дракона")
            if choice_x_1 == "1":
                print("Вы сражаетесь храбро, но дракон оказывается слишком сильным. Вы проиграли.")
                print("game_over")
                return
            else:
                print("Вы бежите обратно по лестнице, но дверь наверху оказывается заперта. Вы в ловушке. Вы проиграли.")
                print("game over")
                return
        else:
            print("Вы решаете не спускаться по лестнице и находите потайную дверь за картиной.")
            choice_x_2 = input("Выбор: 1 - Войти в потайную дверь, 2 - Игнорировать дверь и вернуться назад. ")
            if choice_x_2 == "1":
                print("Потайная дверь приводит вас к выходу из замка. Вы выиграли!")
                return
            else:
                print("На обратной дороге Вы сбились с пути, заблудились и попали в ловушку")
                print("game over")
                return

    choice_0 = input("Введите 1, если хотите открыть сундук или 2 - не открывать сундук и выйти. ")
    if choice_0 == "1":
        print("В сундуке оказывается карта с указанием выхода из замка.")
    else:
        print("Вы выходите из комнаты и попадаете в коридор с двумя новыми дверями.")
        choice_0_1 = input("Выбор: 1 - первая дверь, 2 - вторая дверь")
        if choice_0_1 == "1":
            print("Вы входите в первую дверь и видите старого мага.")
        else:
            print("Вы входите во вторую дверь и видите зеркало, в котором отражается другая комната.")
            spiegel = input("Выбор: 1 - войти в зеркало, 2 - разбить зеркало. ")
            if spiegel == "1":
                print("Вы проходите через зеркало и оказываетесь в другой части замка, где находите выход. Вы выиграли!")
                return
            else:
                print("Зеркало разбивается, и вы оказываетесь в ловушке. Вы проиграли.")
                print("game over")
                return
        choice_0_2 = input("Выбор: 1 - поговорить с магом, 2 - игнортровать мага и выйти. ")
        if choice_0_2 == "1":
            print("Маг дает вам волшебный ключ, который открывает все двери в замке.")
        else:
            print("Вы проигнорировали мага и вышли, после долгих скитаний вы заблудились и оказались в ловушке.")
            print("game over")
            return
        choice_0_3 = input("Выбор: 1 - Использовать ключ для выхода, 2 - Оставить ключ и искать дальше. ")
        if choice_0_3 == "1":
            print("Вы находите дверь, открываете ее ключом и выходите из замка. Вы выиграли!")
            return
        else:
            print("Оставив ключ Вы пошли искать (не понятно чего) дальше. Заблудились и попали в ловушку.")
            print("game over")
            return
    choice_1 = input("Выбор: 1 - Следовать по карте, 2 - игнорировать карту и исследовать комнату. ")
    if choice_1 == "1":
        pass
    else:
        print("После долгих исследований Вы не нашли ничего лучшего, как следовать по карте")

    print("Вы идёте по карте и приходите к тайному проходу")
    choice_2 = input("Выбор: 1 - Войти в проход, 2 - Оставить проход и вернуться назад. ")
    if choice_2 == "1":
        print("Проход приводит вас к выходу из замка. Вы выиграли!")
        return
    else:
        print("На обратном пути Вы заблудились и попали в ловушку.")
        print("game over")
        return

if __name__ == "__main__":
    text_adventure()
    print("Модуль запущен на прямую.")