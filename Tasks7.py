import struct

import unicodedata
# lookup()

def unicode_test(value):
    name=unicodedata.name(value)
    value2= unicodedata.lookup(name)
    print(f"Данное значение = {value}, имя = {name}, символ соответсвующий имени = {value2}")

# unicode_test('E')
# unicode_test('?')
# unicode_test('\u00a2')
# unicode_test('\u0038')
# unicode_test('\u00e9')
# print(ord('&'))

# print(len('$'))
# print(len('\U0001f47b'))

snowman = '\u2603'
# print(len(snowman))
# ds = snowman.encode('utf-8')
# print(ds)
# print(type(ds))
# print(len(ds))

# ds = snowman.encode('ascii', 'replace')
# print(ds)
# print(type(ds))
# print(len(ds))

place = 'caf\u00e9'
# print(place)
# print(type(place))
place_bytes = place.encode('utf-8')
# print(place_bytes)
# print(len(place_bytes))
# print(type(place_bytes))

place2 = place_bytes.decode('utf-8')
# print(place2)

place3 = place_bytes.decode('ascii', 'replace')
# print(place3)

place4 = place_bytes.decode('latin-1')
# print(place4)

place5 = place_bytes.decode('windows-1252')
# print(place5)

actor = 'Richard Gere'
cat = 'Chester'
weight = 28
# print("My wife's favorite actor is %s" % actor)
# print("Our cat %s weighs %s pounds" % (cat, weight))

n = 42
f = 7.03
s = 'string cheese'
# print('%d %f %s' % (n, f, s))
# print('%10d %10f %10s' % (n, f, s))
# print('%-10d %-10f %-10s' % (n, f, s))
# print('%10.4d %10.4f %10.4s' % (n, f, s))
# print('%.4d %.4f %.4s' % (n, f, s))
# print('%*.*d %*.*f %*.*s' % (10, 4, n, 10, 4, f, 10, 4, s))

# d = {'n': 42, 'f': 7.03, 's': 'string cheese'}

# print('{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other'))
# print('{0:d} {1:f} {2:s}'.format(n, f, s))

"""Регулярные выражения"""
import re
# result = re.match('You', 'Young Frankenstein')
youpattern = re.compile('You')
result = youpattern.match('Young Frankenstein')
result2 = youpattern.search('Young Frankenstein')
result3 = youpattern.findall('Young Frankenstein')
# print(result.group())
# print(result2)
# print(result3)

source = 'Young Frankenstein'
m = re.match('You', source) # функция начинает работать с начала источника
# if m:# функция возвращает объект; делайте это, чтобы увидеть, что совпало
#     print(m.group())
#
# m = re.match('^You', source) # якорь в начале строки делает то же самое
# if m:
#     print(m.group())
#
# m = re.match('Frank', source)
# if m:
#     print(m.group())
#
# m = re.search('Frank', source)
# if m:
#     print(m.group())
#
# m = re.match('.*Frank', source)
# if m: # match returns an object
#     print(m.group())

m = re.findall('n', source)
# print(m)
# print('Found', len(m), 'matches')


m = re.findall('n.', source)
# print(m)

m = re.findall('n.?', source)
# print(m)

m = re.findall('.n', source)
# print(m)

m = re.split('n', source)
# print(m)

m = re.sub('n', '?', source)
# print(m)

import string
printable = string.printable
print(printable)

# print(len(printable))
#
# print(re.findall("\d",printable))
# print(re.findall("\w",printable))
# print(re.findall("\s",printable))

tem = 'abc' + '-/*' + '\u00ea' + '\u0115'
# print(re.findall("\w",tem))



# from construct import Struct, Magic, UBInt32, Const, String
#
#
# fmt = Struct('png', Magic(b'\x89PNG\r\n\x1a\n'), UBInt32('length'), Const(String('type', 4), b'IHDR'), UBInt32('width'),UBInt32('height'))
#
# data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
# result = fmt.parse(data)
# print(result)

source = "I wish I may, I wish I might Have a dish of fish tonight."
# print(re.findall('wish', sourse))
# print(re.findall('wish|fish', sourse))
# print(re.findall('^wish', sourse))
# print(re.findall('^I wish', sourse))
# print(re.findall('fish$', sourse))
# print(re.findall('fish tonight.$', sourse))
# print(re.findall('fish tonight\.$', sourse))
# print(re.findall('[wf]ish', sourse))
# print(re.findall('[wsh]', sourse))
# print(re.findall('[wsh]+', sourse))
# print(re.findall('ght\W', sourse))
#
# print(re.findall('I (?=wish)', sourse))
# print(re.findall('(?<=I) wish', sourse))
#
# print(re.findall('\bfish', source))
# print(re.findall(r'\bfish', source))

m = re.search(r'(. dish\b).*(\bfish)', source)
# print(m)

m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
# print(m)

"""Бинарные данные"""
blits=[1,2,3,255]
the_bytes = bytes(blits)
# print(the_bytes)
the_byte_array = bytearray(blits)
# print(the_byte_array)
"""the_bytes[1]=127
print(the_bytes)"""
the_byte_array[1] = 127
# print(the_byte_array)
the_bytes = bytes(range(0, 256))
the_byte_array = bytearray(range(0, 256))
# print(the_bytes)
# print(the_byte_array)

import struct
valid_png_header = b'\x89PNG\r\n\x1a\n'
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
if data[:8] == valid_png_header:
    print(data[:16])
    width, height = struct.unpack('>LL', data[16:24])
    print('Valid PNG, width', width, 'height', height)
else:
    print('Not a valid PNG')

# print(struct.pack('>L', 154))
# print(struct.pack('>L', 141))



import binascii
valid_png_header = b'\x89PNG\r\n\x1a\n'
# print(binascii.hexlify(valid_png_header))
# print(binascii.unhexlify(b'89504e470d0a1a0a'))



print("ПРОВЕРОЧНЫЕ ЗАДАНИЯ")

"""1. Создайте строку Unicode с именем mystery и присвойте ей значение '\U0001f4a9'.
Выведите на экран значение строки mystery. Найдите имя Unicode для mystery."""

mystery = '\U0001f4a9'
print(mystery)
print(unicodedata.name(mystery))

"""2. Закодируйте строку mystery, в этот раз с использованием кодировки UTF-8, в переменную типа bytes с 
именем pop_bytes. Выведите на экран значение переменной pop_bytes."""

pop_bytes = mystery.encode('utf-8')
print(pop_bytes)

"""3. Используя кодировку UTF-8, декодируйте переменную pop_bytes в строку pop_string. 
Выведите на экран значение переменной pop_string. Равно ли оно значению переменной mystery?"""
pop_string = pop_bytes.decode('utf-8')
print(pop_string)
print(pop_string==mystery)
"""4. Запишите следующее стихотворение с помощью старого стиля форматирования. Подставьте строки 'roast beef', 
'ham', 'head' и 'clam' в эту строку:
My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s."""
a='roast beef'
b = 'ham'
c = 'head'
d = 'clam'
print("My kitty cat likes %s,"
      "My kitty cat likes %s,"
      "My kitty cat fell on his %s "
      "And now thinks he's a %s" % (a,b,c,d))

"""5. Запишите следующее письмо по форме с помощью форматирования нового стиля. 
Сохраните строку под именем letter (это имя вы используете в следующем упражнении):

Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please note that it should never be used in a {room}, especially
near any {animals}.
Send us your receipt and {amount} for shipping and handling. We will send
you another {product} that, in our tests, is {percent}% less likely to
have {verbed}.
Thank you for your support.
Sincerely,
{spokesman}
{job_title}"""

letter = "Dear {salutation} {name}," \
         "Thank you for your letter. We are sorry that our {product} {verbed} in your" \
         "{room}. Please note that it should never be used in a {room}, especially" \
         "near any {animals}." \
         "Send us your receipt and {amount} for shipping and handling. We will send" \
         "you another {product} that, in our tests, is {percent}% less likely to" \
         "have {verbed}." \
         "Thank you for your support." \
         "Sincerely," \
         "{spokesman}" \
         "{job_title}"




"""6. Создайте словарь с именем response, имеющий значения для строковых ключей 'salutation', 'name', 'product', 
'verbed' (прошедшее время от глагола verb), 'room', 'animals', 'amount', 'percent', 'spokesman' и 'job_title'. 
Выведите на экран значение переменной letter, в которую подставлены значения из словаря response."""

response = {'salutation': 'Colonel',
            'name': 'Hackenbush',
            'product': 'duck blind',
            'verbed': 'imploded',
            'room': 'conservatory',
            'animals': 'emus',
            'amount': '$1.38',
            'percent': '1',
            'spokesman': 'Edgar Schmeltz',
            'job_title': 'Licensed Podiatrist'}


print(letter.format(**response))

"""7. При работе с текстом вам могут пригодиться регулярные выражения. Мы воспользуемся ими несколькими способами 
в следующем примере текста. Перед вами стихотворение Ode on the Mammoth Cheese, написанное 
Джеймсом Макинтайром (James McIntyre) в 1866 году во славу головки сыра весом 7000 фунтов, которая была сделана в 
Онтарио и отправлена в международное путешествие. Если не хотите вводить это стихотворение целиком, используйте 
свой любимый поисковик и скопируйте его текст в программу. Или скопируйте его из проекта 
«Гутенберг» (http://bit.ly/mcintyre-poetry). Назовите следующую строку mammoth:
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.
Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.
We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon."""

mammoth = "We have seen thee, queen of cheese," \
          "Lying quietly at your ease, " \
          "Gently fanned by evening breeze, " \
          "Thy fair form no flies dare seize. " \
          "All gaily dressed soon you'll go " \
          "To the great Provincial show, " \
          "To be admired by many a beau " \
          "In the city of Toronto. " \
          "Cows numerous as a swarm of bees, " \
          "Or as the leaves upon the trees, " \
          "It did require to make thee please, " \
          "And stand unrivalled, queen of cheese. " \
          "May you not receive a scar as " \
          "We have heard that Mr. Harris " \
          "Intends to send you off as far as " \
          "The great world's show at Paris. " \
          "Of the youth beware of these, " \
          "For some of them might rudely squeeze " \
          "And bite your cheek, then songs or glees " \
          "We could not sing, oh! queen of cheese. " \
          "We'rt thou suspended from balloon, " \
          "You'd cast a shade even at noon, " \
          "Folks would think it was the moon " \
          "About to fall and crush them soon."

"""8. Импортируйте модуль re, чтобы использовать функции регулярных выражений в Python. 
Используйте функцию re.findall(), чтобы вывести на экран все слова, которые начинаются с буквы «с»."""

print(re.findall(r'\bc\w*', mammoth))
pat = r'\bc\w*'
print(re.findall(pat, mammoth))


"""9. Найдите все четырехбуквенные слова, которые начинаются с буквы «c»."""
print(re.findall(r'\bc\w{3}\b', mammoth))

"""10. Найдите все слова, которые заканчиваются на букву «r»."""
print(re.findall(r'\w*r\b', mammoth))
print(re.findall(r'\b\w*r\b', mammoth))
print(re.findall(r'\b\w*l\b', mammoth)) # покажутся ll (от you'll) \w не понимает апостроф
print(re.findall(r'\b[\w\']*l\b', mammoth))
print(re.findall(r"\b[\w']*l\b", mammoth))
"""11. Найдите все слова, которые содержат три гласные подряд."""

print(re.findall(r'\b\w*[aeiou]{3}[^aeiou]\w*\b', mammoth))
print(re.findall(r'\b\w*[aeiou]{3}[^aeiou\s]\w*\b', mammoth))
print(re.findall(r'\b\w*[aeiou]{3}[^aeiou\s]*\w*\b', mammoth)) #+++


"""12. Используйте метод unhexlify для того, чтобы преобразовать шестнадцатеричную строку, 
созданную путем объединения двух строк, что позволило ей разместиться на странице, 
в переменную типа bytes с именем gif:
'47494638396101000100800000000000ffffff21f9' +
'0401000000002c000000000100010000020144003b'"""

her_str = ('47494638396101000100800000000000ffffff21f9' +
           '0401000000002c000000000100010000020144003b')
# gif = binascii.unhexlify(b'47494638396101000100800000000000ffffff21f9'+b'0401000000002c000000000100010000020144003b')
gif = binascii.unhexlify(her_str)
print(gif)
print(len(gif))

"""13. Байты, содержащиеся в переменной gif, определяют однопиксельный прозрачный GIF-файл. Этот формат 
является одним из самых распространенных. Корректный файл формата GIF начинается со строки GIF89a. 
Является ли этот файл корректным?"""

pat_gif = (b'GIF89a')
pat_gif2 = ('GIF89a')
print(pat_gif==gif[:6])
print(pat_gif2==gif[:6])

"""14. Ширина файла формата GIF является шестнадцатибитным целым числом с обратным порядком байтов, которое начинается 
со смещения 6 байт. Его высота имеет такой же размер и начинается со смещения 8 байт. Извлеките и 
выведите на экран эти значения для переменной gif. Равны ли они 1?"""



width, height = struct.unpack('<HH', gif[6:10])
print(width, height)