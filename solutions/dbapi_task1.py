from MySQLdb import connect


connection = connect(host='localhost', user='test', passwd='test', db='test')
cursor = connection.cursor()
cursor.execute('''
SELECT name FROM persons p
WHERE p.id NOT IN (
    SELECT person1_id FROM friends UNION SELECT person2_id FROM friends
)
ORDER BY p.name
''')
for row in cursor.fetchall():
    print row[0]
