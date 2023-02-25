import time

contact_list = ['Бекзод', 'Сарвар', 'Миша', 'Александр', 'Павел']

while True:
    
    answer = input('Что бы вы хотели сделать со списком контактов\n1. Показать список контактов\n2. Добавить контакт\n3. Удалить контакт\n4. Изменить контакт\n5. Очистить список контактов\n')
    if answer == '1':
        contact_list.sort()
        print(contact_list, '\n')
        time.sleep(1)
    elif answer == '2':
        add = input('Введите имя контакта, которого Вы хотите добавить\n')
        contact_list.append(add)
        time.sleep(1)
    elif answer == '3':
        try:
            rem = input('Введите элемент который Вы хотите удалить\n')
            contact_list.remove(rem)
            time.sleep(1)
        except:
            print("Что то пошло не так, возможно имени того, кого вы ввели нет в списке контактов")
            time.sleep(1)
    elif answer == '4':
        izm = input('Введите имя того, кого вы хотите изменить\n')
        index = contact_list.index(izm)
        new = input(f'Введите имя человека кого Вы хотите добавить вместо контакта "{izm}"\n')
        contact_list[index] = new
        time.sleep(1)
    elif answer == '5':
        contact_list.clear()
        time.sleep(1)
    else:
        print('Вы ввели, что то неккоректное')
        time.sleep(1)