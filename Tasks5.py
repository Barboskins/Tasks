# import sys
# from collections import defaultdict
# for place in sys.path:   # Показывает каталог поиска модулей
#     print(place)
#
# print('Program arguments:', sys.argv) # Показывает местонахождение файла
#
# import random
# a= range(10)
# print(random.randint(1,20))

# pereodic_table = {'Hydrogen':1, 'Helium':2}
# print(pereodic_table)
# carbon = pereodic_table.setdefault('carbon',12)
#
# print(pereodic_table)
#
# helium = pereodic_table.setdefault('Helium',947)
# print(helium)
# print(pereodic_table)
# pereodic_table = defaultdict(int)
# print(pereodic_table)
# pereodic_table['Hydrogen'] = 1
# pereodic_table['Lead']
# print(pereodic_table)

"""1. Создайте файл, который называется zoo.py. В нем объявите функцию hours(), которая выводит на экран строку
 ' Open 9-5 daily'. Далее используйте интерактивный интерпретатор, чтобы импортировать модуль zoo и вызвать его функцию hours()."""
# import zoo
# zoo.hours()

"""2. В интерактивном интерпретаторе импортируйте модуль zoo под именем menagerie и вызовите его функцию hours()."""
# import zoo as menagerie
# menagerie.hours()

"""3. Оставаясь в интерпретаторе, импортируйте непосредственно функцию hours() из модуля zoo и вызовите ее."""
# from zoo import hours
# hours()

"""4. Импортируйте функцию hours() под именем info и вызовите ее."""
# from zoo import hours as info
# info()

"""5. Создайте словарь с именем plain, содержащий пары «ключ — значение» 'a': 1, 'b': 2 и 'c':3, а затем выведите его на экран."""
plain = {'a': 1, 'b': 2,'c':3}
# print(plain)

"""6. Создайте OrderedDict с именем fancy из пар «ключ — значение», приведенных в упражнении 5, и выведите его на экран. 
Изменился ли порядок ключей?"""
from collections import OrderedDict
fancy = OrderedDict(plain)
# print(fancy)
"""7. Создайте defaultdict с именем dict_of_lists и передайте ему аргумент list. Создайте список dict_of_lists['a'] и 
присоедините к нему значение 'something for a' за одну операцию. Выведите на экран dict_of_lists['a']."""
from collections import defaultdict
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists)
print(dict_of_lists['a'])
