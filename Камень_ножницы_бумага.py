import time
from random import choice

"""Словарь на случай, если пользователь будет вводить одной буквой, либо случайно латиницей"""
def check_yes_or_no(start):
    dict_ = {"да":['да', 'lf', 'eue', 'угу', 'ага', 'yes', 'yep', 'yea', 'Lf', "д"]}
    for k, v in dict_.items():
        for i in v:
            if me == i:
                return k
            else:
                pass

"""Словарь на случай, если пользователь будет вводить одной буквой, либо случайно латиницей"""
def check_user_choice(me):
    dict_ = {"камень":["к","камень", "r", 'rfvtym'], "ножницы":["н","ножницы", "y", 'yj;ybws'], "бумага":["б","бумага", ",", ',evfuf', "<"]}
    for k, v in dict_.items():
        for i in v:
            if me == i:
                return k
            else:
                pass

"""Эта функция пишет количество баллов у пользователя и компьютера на данный момент"""
def check_score(user_schet, pc_schet):
    if user_schet < 0:
        print(f"Ваш счёт: 0\nСчёт компьютера: {pc_schet}")
    elif pc_schet < 0:
        print(f"Ваш счёт: {user_schet}\nСчёт компьютера: 0")
    else:
        print(f"Ваш счёт: {user_schet}\nСчёт компьютера: {pc_schet}")


while True:
    start = input('Поиграем в Камень/Ножницы/Бумага? (3 попытки)\nДа/Нет? ').lower()

    if check_yes_or_no(start) == "да":
        attempts = 0
        user_schet = 0
        pc_schet = 0

        while attempts < 3:
            pc = choice(['камень', 'ножницы', 'бумага'])
            me = input('Введите Камень(К), Ножиницы(Н) или Бумагу(Б): ').lower()
            user_choice = check_user_choice(me)
            attempts = attempts + 1
            if pc == 'камень' and user_choice == 'бумага':
                print ('Я выбрал Камень. Вы выиграли!!!')
                user_schet = user_schet + 1
                check_score(user_schet, pc_schet)
                time.sleep(1)
            elif pc == 'камень' and user_choice == 'ножницы':
                print('Я выбрал Камень. Вы проиграли.')
                pc_schet = pc_schet + 1
                check_score(user_schet, pc_schet)
                time.sleep(1)
            elif pc == 'ножницы' and user_choice == 'камень':
                print('Я выбрал Ножницы. Вы выиграли!!!')
                user_schet = user_schet + 1
                check_score(user_schet, pc_schet)
                time.sleep(1)
            elif pc == 'ножницы' and user_choice == 'бумага':
                print('Я выбрал Ножницы. Вы проиграли.')
                pc_schet = pc_schet + 1
                check_score(user_schet, pc_schet)
                time.sleep(1)
            elif pc == 'бумага' and user_choice == 'камень':
                print('Я выбрал Бумагу. Вы проиграли!!!')
                pc_schet = pc_schet + 1
                check_score(user_schet, pc_schet)
                time.sleep(1)
            elif pc == 'бумага' and user_choice == 'ножницы':
                print('Я выбрал Бумагу. Вы выиграли.')
                user_schet = user_schet + 1
                check_score(user_schet, pc_schet)
                time.sleep(1)
            elif pc == user_choice:
                print('Я выбрал то же, что и Вы! НИЧЬЯ!')
                check_score(user_schet, pc_schet)
                time.sleep(1)
            else:
                print('Вы ввели, что то некорректное')
                time.sleep(1)
                attempts = attempts - 1

    else:
        print('Через 10 секунд спрошу снова, может быть Вы передумаете))')
        t = 10
        while t > 0:
            t = t-1
            print(f'Ты передумаешь через {t} секунд')
            time.sleep(1)