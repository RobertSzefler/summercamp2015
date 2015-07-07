from __future__ import print_function

from MySQLdb import connect


connection = connect(host='localhost', user='test', passwd='test', db='test')
cursor = connection.cursor()
cursor.execute('SELECT id, name FROM persons')
for id, name in cursor.fetchall():
    print(id, name)
