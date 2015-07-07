from __future__ import print_function
from MySQLdb import connect


connection = connect(host='localhost', user='test', passwd='test', db='test')
cursor = connection.cursor()
cursor.execute('''
SELECT name, balance FROM persons INNER JOIN accounts ON persons.id=accounts.person_id
WHERE balance < (
    SELECT AVG(balance) FROM accounts
)
''')
for name, balance in cursor.fetchall():
    print(name, balance)
