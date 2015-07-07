import random
import warnings

from dbapi_common import cursor

warnings.filterwarnings("ignore", "Unknown table.*")

random.seed(1234)
cursor = cursor()


cursor.execute('DROP TABLE IF EXISTS friends')
cursor.execute('DROP TABLE IF EXISTS accounts')
cursor.execute('DROP TABLE IF EXISTS persons')
cursor.execute('CREATE TABLE persons(id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(30) NOT NULL UNIQUE, age INTEGER NOT NULL)')
cursor.execute("INSERT INTO persons(name, age) VALUES ('Alice', 19)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Bob', 25)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Charlie', 40)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Damian', 27)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Eve', 51)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Felix', 31)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('George', 45)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Henry', 40)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Ian', 20)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Jared', 25)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Kenneth', 60)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Lynda', 35)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Maurice', 41)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Naomi', 26)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Oliver', 22)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Paul', 73)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Quentin', 66)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Rebecca', 25)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Sarah', 18)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Tim', 29)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Ursula', 30)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Vladimir', 55)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Walter', 47)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Xavier', 40)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Yasmine', 24)")
cursor.execute("INSERT INTO persons(name, age) VALUES ('Zane', 53)")

cursor.execute('''CREATE TABLE friends(person1_id INTEGER NOT NULL, person2_id INTEGER NOT NULL,
  FOREIGN KEY(person1_id) REFERENCES persons(id),
  FOREIGN KEY(person2_id) REFERENCES persons(id))''')

cursor.execute('''CREATE TABLE accounts(person_id INTEGER NOT NULL UNIQUE, balance DECIMAL (12,4),
  FOREIGN KEY(person_id) REFERENCES persons(id))''')

for n in range(30):
    p1 = random.randint(1, 26)
    p2 = random.randint(1, 26)
    cursor.execute('INSERT INTO friends(person1_id, person2_id) VALUES (%s, %s)', [p1, p2])

for n in range(1, 27):
    cursor.execute('INSERT INTO accounts(person_id, balance) VALUES (%s, %s)', [n, random.randint(0,1000000)/10000.0])

cursor.execute('COMMIT;')
