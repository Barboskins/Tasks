# fout = open('oops.txt', 'wt')
# print('Oops, I created a file.', file = fout)
# fout.close()

import os
# print(os.path.exists('oops.txt'))
# print(os.path.exists('./oops.txt'))
# print(os.path.exists('waffles'))
# print(os.path.exists('.'))
# print(os.path.exists('..'))

name = 'oops.txt'
# print(os.path.isfile(name))
# print(os.path.isdir('.'))

# print(os.path.isabs(name))
# print(os.path.isabs('/big/fake/name'))
# print(os.path.isabs('big/fake/name/without/a/leading/slash'))

# import shutil
# shutil.copy('oops.txt', 'ohno.txt')

# os.rename('ohno.txt', 'ohwell.txt')

# os.link('oops.txt', 'yikes.txt')
# print(os.path.isfile('yikes.txt'))
# print(os.path.islink('yikes.txt'))
# os.symlink('oops.txt', 'jeepers.txt')
# print(os.path.islink('jeepers.txt'))

# os.chmod('oops.txt', 0o400)  #or
# import stat
# os.chmod('oops.txt', stat.S_IXUSR)

# uid = 5
# gid = 22
# os.chown('ohwell', uid, gid)

# print(os.path.abspath('oops.txt'))
#
# print(os.path.realpath('jeepers.txt'))

# os.remove('oops.txt')
# print(os.path.exists('oops.txt'))

# os.mkdir('poems')
# print(os.path.exists('poems'))

# os.rmdir('poems')
# print(os.path.exists('poems'))

# os.mkdir('poems')
# print(os.listdir('poems'))

# os.mkdir('poems/mcintype')
# print(os.listdir('poems'))

# fout = open('poems/mcintype/the_good_man', 'wt')
# fout.write("""Cheerful and happy was his mood,
# He to the poor was kind and good,
# And he oft' times did find them food,
# Also supplies of coal and wood,
# He never spake a word was rude,
# And cheer'd those did o'er sorrows brood,
# He passed away not understood,
# Because no poet in his lays
# Had penned a sonnet in his praise,
# 'Tis sad, but such is world's ways.
# """)
# fout.close()

# print(os.listdir('poems/mcintype'))

# os.chdir('poems')
# print(os.listdir('.'))

import glob

# print(glob.glob('m*'))
# print(glob.glob('??'))
# print(glob.glob('m??????e'))
# print(glob.glob('[klm]*e'))

# print(os.getpid())
# print(os.getcwd())
# print(os.getuid())
# print(os.getgid())

import subprocess

# ret = subprocess.getoutput('date')
# print(ret)

# ret = subprocess.getoutput('date -u')
# print(ret)

# import calendar
#
# print(calendar.isleap(1900))
# print(calendar.isleap(1996))
# print(calendar.isleap(1999))
# print(calendar.isleap(2000))
# print(calendar.isleap(2002))
# print(calendar.isleap(2004))

from datetime import date

# hallowen = date(2014,10,31)
# print(hallowen)
# print(hallowen.day)
# print(hallowen.month)
# print(hallowen.year)
# print(hallowen.isoformat())
now = date.today()
# print(now)
from datetime import datetime
now = datetime.now()
# print(now)


from datetime import timedelta

# one_day = timedelta(days=1)
# tomorrow = now+one_day
# print(tomorrow)
# print(now+17*one_day)
# yesterday = now - one_day
# print(yesterday)

from datetime import time

# noon = time(12,0,0)
# print(noon)
# print(noon.hour)
# print(noon.minute)
# print(noon.second)
# print(noon.microsecond)

from datetime import datetime, time, date

some_day = datetime(2014, 1, 2, 3, 4, 5, 6)
# print(some_day)
# print(datetime.now())

noon=time(12)
this_day = date.today()
noon_day = datetime.combine(this_day, noon)
# print(noon_day)
# print(noon_day.date())
# print(noon_day.time())

import time

now = time.time()
# print(now)
# print(time.ctime(now))

# print(time.localtime())
# print(time.gmtime())
# tm = time.localtime(now)
# print(tm)
# print(time.mktime(tm))

fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
t = time.localtime()
# print(t)
tm= time.strftime(fmt,t)
# print(tm)

fmt = "%Y-%m-%d"
# print(time.strptime("2012-01-29", fmt))

import locale

# halloween = date(2014, 10, 31)
# for lang_country in ['us', 'fr', 'de', 'es', 'is',]:
#     locale.setlocale(locale.LC_TIME, lang_country)
#     print(halloween.strftime('%A, %B %d'))

"""1. Запишите текущие дату и время как строку в текстовый файл today.txt."""
from datetime import date

# now = datetime.now()
# dt = open('today.txt', 'wt')
# dt.write(str(now))
# dt.close()

now = datetime.today()
now_str = now.isoformat()
# print(now)
# print(type(now_str))
with open('today.txt', 'wt') as f:
    f.write(now_str)


"""2. Прочтите текстовый файл today.txt и разместите данные в строке today_string."""

with open('today.txt', 'rt') as fl:
    today_string = fl.read()

# print(today_string)

"""3. Разберите дату из строки today_string. """

from datetime import datetime
fmt = '%Y-%m-%dT%H:%M:%S.%f'
data = datetime.strptime(today_string, fmt)
# print(data)
# print(type(data))

"""4. Выведите на экран список файлов текущего каталога."""
from pprint import pprint
pprint(os.listdir('.'))