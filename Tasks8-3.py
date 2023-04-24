"1. Присвойте строку 'This is a test of the emergency text system' переменной test1 и запишите переменную test1 в файл с именем test.txt."

test1= 'This is a test of the emergency text system'


with open ('test', 'wt') as f:
    f.write(test1)


"2. Откройте файл test.txt и считайте его содержимое в строку test2. Совпадают ли строки test1 и test2?"

with open ('test', 'rt') as f:
    test2=f.read()
# print(test2)

"3. Сохраните следующие несколько строк в файл books.csv. Обратите внимание на то, что, если поля разделены запятыми, " \
"вам нужно заключить поле в кавычки, если оно содержит запятую:" \
"author,book " \
"J R R Tolkien,The Hobbit " \
"Lynne Truss,'Eats, Shoots & Leaves'"
import csv

text = """author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"
"""

# with open('books.csv', 'wt') as f:
#     f.write(text)
# print(len(text))

# values=[
#     ['author', 'book'],
#     ['J R R Tolkien','The Hobbit'],
#     ['Lynne Truss','Eats, Shoots & Leaves']
# ]

# with open ('books', 'wt', newline='') as f:
#     data = csv.writer(f)
#     data.writerows(values)





"4. Используйте модуль csv и его метод DictReader, чтобы считать содержимое файла books.csv в переменную books. " \
"Выведите на экран значения переменной books. Обработал ли метод DictReader кавычки и запятые в заголовке второй книги?"

# with open('books.csv', 'rt') as f:
#     books = csv.DictReader(f)
#     for book in books:
#         print(book)



"5. Создайте CSV-файл books.csv и запишите его в следующие строки:" \
"title,author,year " \
"The Weirdstone of Brisingamen,Alan Garner,1960 " \
"Perdido Street Station,China Miéville,2000 " \
"Thud!,Terry Pratchett,2005 " \
"The Spellman Files,Lisa Lutz,2007 " \
"Small Gods,Terry Pratchett,1992"

data ="""title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992"""

with open('books.csv', 'wt', encoding= 'utf-8') as f:
   f.write(data)


"6. Используйте модуль sqlite3, чтобы создать базу данных SQLite books.db и таблицу books, содержащую следующие поля: " \
"title (text), author (text) и year (integer)."
import sqlite3

# conn = sqlite3.connect('books.db')
# curs = conn.cursor()
# curs.execute("""CREATE TABLE IF NOT EXISTS books
# (title text,
#  author text,
#  year int)""")
# conn.commit()

"7. Считайте данные из файла books.csv и добавьте их в таблицу book."
ins_str = 'INSERT INTO books VALUES (?, ?, ?)'

# with open('books.csv', 'rt', encoding= 'utf-8') as f:
#    books = csv.DictReader(f)
#    for book in books:
#        conn.execute(ins_str, (book['title'], book['author'], book['year']))
#
# conn.commit()
"8. Считайте и выведите на экран графу title таблицы book в алфавитном порядке."
# curs.execute('SELECT title FROM books ORDER BY title ')
# rows = curs.fetchall()
# for row in rows:
#     print(row)
"9. Считайте и выведите на экран все графы таблицы book в порядке публикации."
# curs.execute('SELECT * FROM books ORDER BY year ')
# rows = curs.fetchall()
# for row in rows:
#     print(row)

"10. Используйте модуль sqlalchemy, чтобы подключиться к базе данных sqlite3 books.db, которую вы создали в " \
"упражнении 6. Как и в упражнении 8, считайте и выведите на экран графу title таблицы book в алфавитном порядке."
#import sqlalchemy as sa
#
# db = sa.create_engine('sqlite:///books.db')
# conn = db.connect()

# rows = conn.execute(sa.text('SELECT title FROM books ORDER BY title '))
# # print(rows.fetchall())
# for row in rows:
#     print(row[0])

# rows = conn.execute(sa.text('SELECT * FROM books ORDER BY year '))
# print(rows.fetchall())
# for row in rows:
#     print(row)

"11. Установите сервер Redis и библиотеку Python redis (с помощью команды pip install redis) на свой компьютер. " \
"Создайте хеш redis с именем test, содержащий поля count (1) и name ('Fester Bestertester'). Выведите все поля хеша test."




"12. Увеличьте поле count хеша test и выведите его на экран."