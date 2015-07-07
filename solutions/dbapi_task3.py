from __future__ import print_function
from MySQLdb import connect
import sys


person_name = sys.argv[1]

connection = connect(host='localhost', user='test', passwd='test', db='test')
cursor = connection.cursor()
cursor.execute('''
SELECT ppp.name, a.balance FROM persons p, persons pp, persons ppp, friends f, friends ff, accounts a
WHERE p.name=%s AND
  f.person1_id=p.id AND
  pp.id=f.person2_id AND
  ff.person1_id=pp.id AND
  ppp.id=ff.person2_id AND
  a.person_id=ppp.id
''', [person_name])

for name, balance in cursor.fetchall():
    print(name, balance)
