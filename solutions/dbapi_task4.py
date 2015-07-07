from __future__ import print_function
from MySQLdb import connect
import sys


name1 = sys.argv[1]
name2 = sys.argv[2]

connection = connect(host='localhost', user='test', passwd='test', db='test')
connection.autocommit(True)
cursor = connection.cursor()
cursor.execute('''
DELETE FROM friends WHERE person1_id=(
    SELECT id FROM persons WHERE name=%s
)
AND person2_id=(
    SELECT id FROM persons WHERE name=%s
)
''', [name1, name2])
