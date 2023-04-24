# poem = "There was a young lady named Bright, \n" \
#        "Whose speed was far faster than light; \n" \
#        "She started one day \n" \
#        "In a relative way, \n" \
#        "And returned on the previous night."

# print(len(poem))

# f = open('relativity', 'wt')
# f.write(poem)
# print(poem, file = f)
# print(poem, file = f, sep = '', end = '')
# f.close()

# fin = open('relativity', 'rt')
# pem = fin.read()
# f.close
#
# print(pem)
# print(len(pem))

# poem = ''
# fin = open('relativity', 'rt' )
# chunk = 100
# while True:
#        fragment = fin.read(chunk)
#        print(fragment)
#        print(len(fragment))
#        if not fragment:
#               break
#        poem +=fragment
# fin.close()

# print(poem)

# poem = ''
# fin = open('relativity', 'rt' )
# while True:
#        line = fin.readline()
#        print(line)
#        # print(len(line))
#        if not line:
#               break
#        poem +=line
# fin.close()


# poem = ''
# fin = open('relativity', 'rt' )
# lines = fin.readlines()
# print(len(lines))
# for line in lines:
#        print(line, end='')


# bdata = bytes(range(0,256))
# print(len(bdata))
#
# file = open('bdata', 'wb')
# file.write(bdata)
# file.close()
#
# fin = open('bdata', 'rb')
# bdata2 = fin.read()
# fin.close()
# print(bdata2)
# print(len(bdata2))

# with open('relativity', 'wt') as f:
#        f.write(poem)


# fin = open('bdata', 'rb')
# print(fin.read())
# print(fin.tell())
# fin.seek(255)
# print(fin.seek(255))
# bd = fin.read()
# print(bd)
# print(bd[0])
# print(len(bd))

# print(fin.seek(-1,2))

"""СТРУКТУРИРОВАННЫЕ ТЕКСТОВЫЕ ФАЙЛЫ"""

"""Файлы с разделителями"""

import csv

villains = [['Doctor', 'No'],['Rosa', 'Kleeb'],['Mister', 'Big'],['Auric', 'Goldfinger'],['Ernst', 'Blofeld']]

# with open('villains', 'wt', newline='') as f:
#        csvvout = csv.writer(f)
#        csvvout.writerows(villains)

with open('villains', 'rt') as file:
       cin = csv.reader(file)
       villains = [row for row in cin]

# print(villains)

with open('villains', 'rt') as file:
       cin = csv.DictReader(file)
       villains = [row for row in cin]

# print(villains)

with open('villains', 'rt') as file:
       cin = csv.DictReader(file, fieldnames=['first', 'last'])
       villains = [row for row in cin]

# print(villains)

villains2 = [{'first': 'Doctor', 'last': 'No'},
             {'first': 'Rosa', 'last': 'Klebb'},
             {'first': 'Mister', 'last': 'Big'},
             {'first': 'Auric', 'last': 'Goldfinger'},
             {'first': 'Ernst', 'last': 'Blofeld'}
             ]

with open('villains2', 'wt', newline='') as fin:
       cout = csv.DictWriter(fin, ['first', 'last'],)
       cout.writeheader()
       cout.writerows(villains2)

with open('villains2', 'rt') as file:
    cin = csv.DictReader(file)
    villains2 = [row for row in cin]
# print(villains2)

"""Файл формата разметка XML"""

import xml.etree.ElementTree as et

tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
# print(root.tag)

# for child in root:
#     print('tag:', child.tag, 'attributes:', child.attrib)
#     for grandchild in child:
#         print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)

# print(len(root))
# print(len(root[0]))

"""Формат JSON"""

menu = \
{
"breakfast":{
    "hours": "7-11",
    "items": {
        "breakfast burritos": "$6.00",
        "pancakes": "$4.00"
        }
    },
"lunch" :{
    "hours": "11-3",
    "items": {
        "hamburger": "$5.00"
        }
    },
"dinner": {
    "hours": "3-10",
    "items": {
        "spaghetti": "$8.00"
        }
    }
}
# print(type(menu))

import json

menu_json = json.dumps(menu)
# print(menu_json)
# print(type(menu_json))

menu2= json.loads(menu_json)
# print(menu2)
# print(type(menu2))


import datetime
now = datetime.datetime.utcnow()
# print(now)
# json.dumps(now)
now_str = str(now)
json.dumps(now_str)

from time import mktime
now_epoch = int(mktime(now.timetuple()))
ne=json.dumps(now_epoch)
# print(ne)


class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        # isinstance() проверяет тип объекта
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))
        # иначе это то, что знает обычный декодер:
        return  json.JSONEncoder.default(self, obj)



# print(json.dumps(now, cls=DTEncoder))


"""Формат YAML"""

import yaml
from yaml.loader import SafeLoader

with open('mcintype.yaml', 'rt') as fin:
    text = fin.read()

data = yaml.load(text, Loader=SafeLoader)
# print(data['details'])
# print(len(data['poems']))
# print(data['poems'][1]['title'])


import pickle
now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled)
# print(now1)
# print(pickled)
# print(now2)

class Tiny():
    def __str__(self):
        return 'tiny'

obj1=Tiny()
# print(str(obj1))
# print(type(str(obj1)))

pikled = pickle.dumps(obj1)
print(pikled)
obj2= pickle.loads(pikled)
# print(str(obj2))
# print(type(str(obj2)))

