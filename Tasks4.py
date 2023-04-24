"""1. Присвойте значение 7 переменной guess_me. Далее напишите условные проверки (if, else и elif), чтобы вывести
строку 'too low', если значение переменной guess_me меньше 7, 'too high', если оно больше 7, и 'just right',
если равно 7."""

# guess_me = 7
# if guess_me < 7:
#     print('too low')
# elif guess_me > 7:
#     print('too high')
# else:
#     print('just right')



"""2. Присвойте значение 7 переменной guess_me и значение 1 переменной start. Напишите цикл while, который сравнивает 
переменные start и guess_me. Выведите строку 'too low', если значение переменной start меньше значения переменной 
guess_me. Если значение переменной start равно значению переменной guess_me, выведите строку 'found it!' и выйдите 
из цикла. Если значение переменной start больше значения переменной guess_me, выведите строку 'oops' и выйдите из цикла. 
Увеличьте значение переменной start на выходе из цикла."""

guess_me = 7
start = 1
while True:
    if start < guess_me:
        print('too low')
    elif  start == guess_me:
        print('found it')
        break
    else:
        print('oops')
        break
    start += 1

"""3. Используйте цикл for, чтобы вывести на экран значения списка [3, 2, 1, 0]."""

list_range = [3, 2, 1, 0]
for el in list_range:
    print(el)

"""4. Используйте включение списка, чтобы создать список, который содержит нечетные числа в диапазоне range(10)."""

# list_1 = []
# for el in range(10):
#     if el % 2 != 0:
#         list_1.append(el)
# print(list_1)

even = [number for number in range(10) if number % 2 != 0]
print(even)

"""5. Используйте включение словаря, чтобы создать словарь squares. Используйте вызов range(10), чтобы получить ключи, 
и возведите их в квадрат, чтобы получить их значения."""

squares = {number: number*number for number in range(10)}
print(squares)

"""6. Используйте включение множества, чтобы создать множество odd, которое содержит четные числа 
в диапазоне range(10)."""

odd = {number for number in range(10) if number % 2 == 0}
print(odd)

"""7. Используйте включение генератора, чтобы вернуть строку 'Got' и количество чисел в диапазоне range(10). 
Итерируйте по нему с помощью цикла for."""

# iter_gener = (number for number in range(10))
#
# for el in iter_gener:
#     print(el)

for thing in ('Got %s' % number for number in range(10)):
    print(thing)

# days = ['M', 'T', "W"]
# fruits = ['b', 'o', 'p']
# drinks = ['c', 't', 'b']
#
# for day, fruit, drink in zip(days, fruits, drinks):
#     print(day, ':drink', drink, ', eat', fruit)
#
# number_list = [number for number in range(1,6)]
# print(number_list)

# def buggy (arg, result =[]):
#     result.append(arg)
#     print(result)
#
# buggy('a')
# buggy('b')

# def edit_story(words, func):
#     for word in words:
#         print(func(word))
#
# stairs = ['thur', 'meow', 'thud', 'hiss']

# def enliven(br):
#     return br.capitalize() + '!'
#
# edit_story(stairs, enliven)

# edit_story(stairs, lambda br: br.capitalize() + '!')

# def my_range(start=0, end=10):
#     while start < end:
#         yield start
#         start += 1
#
# print(type(my_range))
# result= my_range()
#
# print(result)

# def document_it(func):
#     def new_function(*args,**kwargs):
#         print('Running function1:' , func.__name__)
#         print('Positional arguments:', args)
#         print('keyword arguments:', kwargs)
#         result = func(*args,**kwargs)
#         print('Result1:', result )
#         return result
#     return new_function
#
# def square_it(func):
#     def new_function2(*args,**kwargs):
#         print('Running function2:', func.__name__)
#         result = func(*args,**kwargs)
#         print('Result2:', result)
#         return result * result
#     return new_function2
#
# @document_it
# @square_it
# def add_ints(a,b):
#     return a+b
#
# print(add_ints(3,5))
#
# print('')
# print('ТЕПЕРЬ НАОБОРОТ')
# print('')
#
# @square_it
# @document_it
# def add_ints(a,b):
#     return a+b
#
# print(add_ints(3,5))



animal = 'fruitbat'

# def print_global():
#     print('fdfdf:',animal)
#
# print_global()

# def change_and_print_global():
#     global animal
#     animal = 'wombat'
#     print('vsfsfsf:', animal)
#
# print(animal)
# change_and_print_global()
#
# print(animal)

