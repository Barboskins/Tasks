"""1. Создайте список years_list, содержащий год, в который вы родились, и каждый последующий год вплоть
до вашего пятого дня рождения. Например, если вы родились в 1980 году, список будет выглядеть так:
years_list =[1980, 1981, 1982, 1983, 1984, 1985] """

years_list =[1993, 1994, 1995, 1996, 1997, 1998]

"""2. В какой из годов, содержащихся в списке years_list, был ваш третий день рождения. 
Помните в первый год вам было 0 лет """

print(years_list[3])

"""3. В каком из годов, содержащихся в списке years_list вам было больше всего лет """

print(years_list[len(years_list)-1])
print(years_list[-1])
print(years_list[5])

"""4. Создайте список things, содержащий три элемента mozzarella, cinderella, salmonella """

things = ['mozzarella', 'cinderella', 'salmonella']

"""5. Напишите с большой буквы тот элемент из списка things, который относится к человеку, а затем выведите список. 
  Изменился ли элемент списка?"""
print(things[1].capitalize())
print(things)

things[1] = things[1].capitalize() #если надо его заменить в списке
print(things)

"""6. Переведите сырный элемент списка things в верхний регистр целиком и выведите список """
print(things[0].upper())
things[0] = things[0].upper() #если надо его заменить в списке
print(things)

"""7. Удалите болезнь из списка things и выведите список на экран """
things.remove('salmonella')
print(things)
#можно указать del things[-1] или del things[2]

"""8. Создайте список surprise, содержащий элементы Groucho, Chico, Harpo """
surprise = ['Groucho', 'Chico', 'Harpo']

"""9. Напишите последний элемент списка surprise со строчной буквы, затем обратите его и напишите с прописной """
lowercase_word = surprise[-1].lower()
print(lowercase_word)
cap_world = lowercase_word[::-1].capitalize()
print(cap_world)

"""10. Создайте англо-французский словарь e2f и выведите его на экран. Слова dog/chien, cat/chat, walrus/morse  """
e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse' }

"""11. Используя словарь e2f и выведите французский вариант слова  walrus """
print(e2f['walrus'])

"""12. Создайте франзуско-английский  словарь f2e на основе словаря e2f. Используйте метод items """
# f2e = {'chien':'dog', 'chat':'cat', 'morse':'walrus' }
# print(f2e.items())

f2e = {}
for english, franch in e2f.items():
    f2e[franch] = english
print('новый словарь', f2e)


"""13. Используя  словарь f2e выведите англ вариант chien """
print(f2e['chien'])

"""14. Создайте и выведите на экран множество анг слов из ключей сдоваря e2f """
set_word_key = set(e2f.keys())
print(set_word_key)

"""15. Создайте многоуровневый словарь life. Используйте следующие строки для ключей верхнего уровня animals, plants, 
other.  Сделайте так, чтобы ключ animals ссылался на другой словарь, имеюший ключи cats, octopi, emus. Сделайте так
чтобы ключ cats ссылался на список строк со значениями Henri, Grumpy, Lucy. Остальные ключи должны ссалаться на пустые словари"""
list_cats = ['Henri', 'Grumpy', 'Lucy']

dict_animals = {'cats':list_cats, 'octopi':{}, 'emus':{}}

life = {'animals':dict_animals, 'plants': {}, 'other':{}}

"""16. Выведите на экран высокоуровневые ключи life """
print(life.keys())

"""17. Выведите на экран  ключи life[animals] """
print(life['animals'].keys())

"""18. Выведите на экран  значение life[animals][cats] """
print(life['animals']['cats'])