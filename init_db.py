import random

from sa_common import session, engine


random.seed(1234)


engine.execute('DROP TABLE IF EXISTS friends')
engine.execute('DROP TABLE IF EXISTS accounts')
engine.execute('DROP TABLE IF EXISTS persons')
engine.execute('CREATE TABLE persons(id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(30) NOT NULL UNIQUE, age INTEGER NOT NULL)')
engine.execute("INSERT INTO persons(name, age) VALUES ('Alice', 19)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Bob', 25)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Charlie', 40)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Damian', 27)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Eve', 51)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Felix', 31)")
engine.execute("INSERT INTO persons(name, age) VALUES ('George', 45)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Henry', 40)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Ian', 20)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Jared', 25)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Kenneth', 60)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Lynda', 35)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Maurice', 41)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Naomi', 26)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Oliver', 22)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Paul', 73)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Quentin', 66)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Rebecca', 25)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Sarah', 18)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Tim', 29)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Ursula', 30)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Vladimir', 55)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Walter', 47)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Xavier', 40)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Yasmine', 24)")
engine.execute("INSERT INTO persons(name, age) VALUES ('Zane', 53)")

engine.execute('''CREATE TABLE friends(person1_id INTEGER NOT NULL, person2_id INTEGER NOT NULL,
  FOREIGN KEY(person1_id) REFERENCES persons(id),
  FOREIGN KEY(person2_id) REFERENCES persons(id))''')

engine.execute('''CREATE TABLE accounts(person_id INTEGER NOT NULL UNIQUE, balance DECIMAL (12,4),
  FOREIGN KEY(person_id) REFERENCES persons(id))''')

for n in range(30):
    p1 = random.randint(1, 26)
    p2 = random.randint(1, 26)
    engine.execute('INSERT INTO friends(person1_id, person2_id) VALUES (%s, %s)', p1, p2)

for n in range(1, 27):
    engine.execute('INSERT INTO accounts(person_id, balance) VALUES (%s, %s)', n, random.randint(0,1000000)/10000.0)
