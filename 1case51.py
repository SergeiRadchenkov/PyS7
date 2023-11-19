'''
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.
Ввод:
values = [0, 2, 10, 6] 
if same_by(lambda x: x % 2, values):
print(‘same’)
else:
print(‘different’)
Вывод:
same
'''
values = [0, 2, 10, 6]
same_by = list(filter(lambda a: True if a % 2 == 0 else False, values))
if len(values) == len(same_by):
    print('same')
else:
    print('different')

# Вариант 2

values = [1, 3, 5, 7]
def same_by(characteristic, objects):
    return len(set(map(characteristic, objects))) < 2

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different') 