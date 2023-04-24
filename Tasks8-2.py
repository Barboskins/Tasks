"""РЕЛЯЦИОННЫЕ БАЗЫ ДАННЫХ"""

# import sqlite3

# conn = sqlite3.connect('enterprice.db')
# curs = conn.cursor()
# curs.execute("""CREATE TABLE IF NOT EXISTS zoo
# (critter VARCHAR(20) PRIMARY KEY,
# count INT,
# damages FLOAT)""")
#
# curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
# curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')
#
# ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
# curs.execute(ins, ('weasel', 1, 2000.0))
#
# result=curs.execute('SELECT*FROM zoo')
#
# # print(result.fetchone())
# # print(result.fetchall())
#
# res_order_up = curs.execute('SELECT*FROM zoo ORDER BY count')
# # print(res_order_up.fetchall())
#
# res_order_down = curs.execute('SELECT*FROM zoo ORDER BY count DESC')
# # print(res_order_down.fetchall())
#
# # res_order_dam = curs.execute('SELECT*FROM zoo ORDER BY damages DESC')
# # print(res_order_dam.fetchone())
#
# res_order_dam = curs.execute('SELECT*FROM zoo WHERE damages = (SELECT MAX(damages) FROM zoo)')
# # print(res_order_dam.fetchall())
#
# curs.close()
# conn.close()
import sqlalchemy
import sqlalchemy as sa
"""Третий уровень SQLAlchemy"""

# conn = sa.create_engine('sqlite:///some.db')
# connection = conn.connect()

# sql_query = sa.text("""CREATE TABLE IF NOT EXISTS zoo
# (critter VARCHAR(20) PRIMARY KEY,
# count INT,
# damages FLOAT)""")
#
# connection.execute(sql_query)
#
# connection.execute(sa.text('INSERT INTO zoo VALUES("duck", 10, 0.0)'))
# connection.execute(sa.text('INSERT INTO zoo VALUES("bear", 2, 1000.0)'))
# connection.execute(sa.text('INSERT INTO zoo VALUES("weasel", 1, 2000.0)'))
#
# rows = connection.execute(sa.text('SELECT * FROM zoo'))
# # print(rows.fetchall())
# for row in rows:
#     print(row)
####################
"""Второй уровень SQLAlchemy"""

# conn = sa.create_engine('sqlite://')
# connection = conn.connect()
#
# meta = sa.MetaData()
# zoo = sa.Table('zoo', meta,
#                sa.Column('critter', sa.String, primary_key=True),
#                sa.Column('count', sa.Integer),
#                sa.Column('damages', sa.Float)
#                )
#
# meta.create_all(connection)
#
# connection.execute(zoo.insert().values(("bear", 2, 1000.0)))
# connection.execute(zoo.insert().values(("weasel", 1, 2000.0)))
# connection.execute(zoo.insert().values(("duck", 10, 0.0)))
#
# result = connection.execute(zoo.select())
# print(result.fetchall())3

# ####################
"""Первый уровень SQLAlchemy"""
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# conn = sa.create_engine('sqlite:///zoo.db')
# connection = conn.connect()
#
# Base = sa.orm.declarative_base()
#
# class Zoo(Base):
#     __tablename__ = 'zoo'
#     critter = sa.Column('critter', sa.String, primary_key=True)
#     count = sa.Column('count', sa.Integer)
#     damages = sa.Column('damages', sa.Float)
#     def __init__(self, critter, count, damages):
#         self.critter = critter
#         self.count = count
#         self.damages = damages
#     def __repr__(self):
#         return "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages)


# Base.metadata.create_all(connection)
#
# first = Zoo('duck', 10, 0.0)
# second = Zoo('bear', 2, 1000.0)
# third = Zoo('weasel', 1, 2000.0)
#
# Session = sessionmaker(bind=connection)
# session = Session()
#
# session.add(first)
# session.add_all([second, third])
# session.commit()

"""Семейство dbm"""
# import dbm
#
# db = dbm.open('definitions', 'c')
#
# db['mustard'] = 'yellow'
# db['ketchup'] = 'red'
# db['pesto'] = 'green'
#
# # print(len(db))
# # print(db['pesto'])
#
# db.close()
#
# db = dbm.open('definitions', 'r')
# print(db['mustard'])

"""Memcached"""
# import memcache
#
# db = memcache.Client(['127.0.0.1:11211'])
# db.set('marco', 'polo')
# print(db.get('marco'))

"""Redis"""
import redis

# conn = redis.Redis('localhost', 6379)
# print(conn.keys('*'))
