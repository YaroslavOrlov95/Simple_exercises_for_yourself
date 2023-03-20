dict = {'1': '4', '2': '1', '4': '3', '3': '2'}
voz = [sorted(dict.items(), key=lambda x: x[1])]
ub = [sorted(dict.items(), key=lambda x: x[1], reverse=True)]
print(f'Оригинальный словарь {dict}')
print(f'Значения по возрастанию {voz}')
print(f'Значения по убыванию {ub}')
