class Car():
    def exclaim(self):
        print("I'm a Car!")
    pass

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car")
    def need_a_push(self):
        print('A little help here?')

give_car = Car()
give_yugo = Yugo()

# give_car.exclaim()
# give_yugo.exclaim()
# give_yugo.need_a_push()
# give_car



class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


class Doctor(Person):
    def __init__(self, name):
        self.name = 'Doctor ' + name

class Advocate(Person):
    def __init__(self, name):
        self.name = name + ' Esquire'

Man = Person('Fudd')
Doc = Doctor('Dudd')
Law = Advocate('Ludd')
bob = EmailPerson('Bob Frapples', 'bob@test.ru')

# print(bob.name)
# print(bob.email)
# print(Man.name)
# print(Doc.name)
# print(Law.name)


class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)

# fowl = Duck('Howard')
# print(fowl.name)
# print(fowl.get_name())
#
# fowl.name = 'Daffy'
# print(fowl.name)
# print(fowl.set_name('Daffy'))
# print(fowl.name)

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


# fowl = Duck('Howard')
# print(fowl.name)
#
# print(fowl.hidden_name)
#
# fowl.name = 'Daffy'
# print(fowl.name)
#
# print(fowl.hidden_name)

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

# c = Circle(5)
# print(c.radius)
# print(c.diameter)
# c.radius = 7
# print(c.diameter)
# c.diameter = 10

class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name

# fowl = Duck('Howard')
# print(fowl.name)
#
# fowl.name = 'Donald'
# print(fowl.name)


class A():
    count = 0
    def __init__(self):
        A.count +=1
    def exlaim(self):
        print("I'm an A")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")


# a = A()
# b = A()
# c = A()
# print(A.count)
# A.kids()
# print(a.kids())

class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')

# a = CoyoteWeapon()
# a.commercial()
# CoyoteWeapon.commercial()

class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
# print(hunter.who(), 'says:', hunter.says())
#
hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
# print(hunted1.who(), 'says:', hunted1.says())
#
hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
# print(hunted2.who(), 'says:', hunted2.says())

class BabblingBrook():
    def who(self):
        return 'Brook'
    def says(self):
        return 'Babble'

brook =  BabblingBrook()

def who_says(obj):
    print(obj.who(), 'says', obj.says())

# who_says(hunter)
# who_says(hunted1)
# who_says(hunted2)
# who_says(brook)

class Word():
    def __init__(self, text):
        self.text=text
    def equals(self, word2):
        return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('HA')
third = Word('eh')

# print(first.equals(second))
# print(third.equals(second))

class Word():
    def __init__(self, text):
        self.text=text
    def __eq__(self, other):
        return self.text.lower() == other.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return self.text

first = Word('ha')
second = Word('HA')
third = Word('eh')

# print(first == second)
# print(first == third)
# first
# print(first)

class Bill():
    def __init__(self, description):
        self.description = description


class Tail():
    def __init__(self, length):
        self.length = length

# class Duck():
#     def __init__(self, bill, tail):
#         self.bill = bill
#         self.tail = tail
#     def about(self):
#         print('This duck has a', bill.description, 'bill and a',
#               tail.length, 'tail')

# tail = Tail('long')
# bill = Bill('wide orange')
# duck = Duck(bill, tail)
# duck.about()

from collections import namedtuple

Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')

# print(duck)
# print(duck.bill)
# print(duck.tail)

parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
# print(duck2)

duck3 = duck2._replace(tail='magnificent', bill='crushing')
# print(duck3)

"""1. Создайте класс, который называется Thing, не имеющий содержимого, и выведите его на экран. 
Затем создайте объект example этого класса и также выведите его. Совпадают ли выведенные значения?"""
class Thing():
    pass
example = Thing()

# print(Thing)
# print(example)
"""2. Создайте новый класс с именем Thing2 и присвойте его атрибуту letters значение 'abc'. 
Выведите на экран значение атрибута letters."""
class Thing2():
    letters = 'abc'

# print(Thing2.letters)
"""3. Создайте еще один класс, который, конечно же, называется Thing3. В этот раз присвойте значение 'xyz' атрибуту 
объекта, который называется letters. Выведите на экран значение атрибута letters. Понадобилось ли вам создавать 
объект класса, чтобы сделать это?"""
class Thing3():
    def __init__(self):
        self.letters = 'xyz'

test = Thing3()
# print(test.letters)

"""4. Создайте класс, который называется Element, имеющий атрибуты объекта name, symbol и number. 
Создайте объект этого класса со значениями 'Hydrogen', 'H' и 1."""

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

elem = Element('Hydrogen', 'H', 1)
# print(elem.name)
# print(elem.symbol)
# print(elem.number)

"""5. Создайте словарь со следующими ключами и значениями: 'name': 'Hydrogen', 'symbol': 'H', 'number': 1. 
Далее создайте объект с именем hydrogen класса Element с помощью этого словаря"""
el = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1.}
hydrogen = Element(**el) #если ключи не совпадают с названием атрибута объектов класса то hydrogen = Element(el['name'], el['symbol'], el['number'])
# hydrogen = Element(el['name'], el['symbol'], el['number'])
# print(hydrogen.name)
# print(hydrogen.symbol)
# print(hydrogen.number)

"""6. Для класса Element определите метод с именем dump(), который выводит на экран значения атрибутов объекта 
(name, symbol и number). Создайте объект hydrogen из этого нового определения и используйте метод dump(), 
чтобы вывести на экран его атрибуты."""

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        return f'Имя элемента - {self.name}, обозначение - {self.symbol}, порядковый номер {self.number}'


hydrogen = Element(**el)
# print(elem.dump())

"""7. Вызовите функцию print(hydrogen). В определении класса Element измените имя метода dump на __str__, 
создайте новый объект hydrogen и затем снова вызовите метод print(hydrogen)."""
# print(hydrogen)

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return f'Имя элемента - {self.name}, обозначение - {self.symbol}, порядковый номер {self.number}'

hydrogen = Element(**el)
# print(hydrogen.name)

"""8. Модифицируйте класс Element, сделав атрибуты name, symbol и number закрытыми. 
Определите для каждого атрибута свойство получателя, возвращающее значение соответствующего атрибута."""

class Element():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number

    def __str__(self):
        return f'Имя элемента - {self.__name}, обозначение - {self.__symbol}, порядковый номер {self.__number}'

hydrogen = Element(**el)
# print(hydrogen.name)
# print(hydrogen.symbol)
# print(hydrogen.number)

"""9. Определите три класса: Bear, Rabbit и Octothorpe. Для каждого из них определите всего один метод — eats(). 
Он должен возвращать значения 'berries' (для Bear), 'clover' (для Rabbit) или 'campers' (для Octothorpe). 
Создайте по одному объекту каждого класса и выведите на экран то, что ест указанное животное."""

class Bear():
    def eats(self):
        return 'berries'

class Rabbit():
    def eats(self):
        return 'clover'

class Octothorpe():
    def eats(self):
        return 'campers'

b = Bear()
r = Rabbit()
o = Octothorpe()
# print(b.eats())
# print(r.eats())
# print(o.eats())

"""10. Определите три класса: Laser, Claw и SmartPhone. Каждый из них имеет только один метод — does(). 
Он возвращает значения 'disintegrate' (для Laser), 'crush' (для Claw) или 'ring' (для SmartPhone). 
Далее определите класс Robot, который содержит по одному объекту каждого из этих классов. 
Определите метод does() для класса Robot, который выводит на экран все, что делают его компоненты."""

class Laser():
    def does(self):
        return 'disintegrate'

class Claw():
    def does(self):
        return 'crush'

class SmartPhone():
    def does(self):
        return 'ring'


class Robot():
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
    def does(self):
        return 'Мои компоненты : Лазер %s.' \
               ' Коготь %s. Телефон %s' %(self.laser.does(), self.claw.does(),self.smartphone.does())


rob = Robot()
print(rob.does())