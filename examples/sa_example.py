from __future__ import print_function

from sqlalchemy import Column, Integer, String, UniqueConstraint
from sa_common import Base, session


### DDL

class Person(Base):
    __tablename__ = 'persons'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    __table_args__ = (
        UniqueConstraint('name'),
    )


### SELECT queries

all_persons = session.query(Person)
filtered_persons = session.query(Person).filter(Person.name > 'Leonardo').order_by(Person.name)

print('COUNT(*): {}\n------'.format(all_persons.count()))
print('Filtered COUNT(*): {}\n------'.format(filtered_persons.count()))
print('Query:\n{}\n------'.format(filtered_persons))

for person in filtered_persons:
    print(person.name)

print('------')

other_persons = session.query(Person).filter(Person.name.ilike('%la%'))

for person in other_persons:
    print(person.name)


### Inserts and updates

session.query(Person).filter(Person.name=='Marylin').delete()
session.query(Person).filter(Person.name=='Phoebe').delete()

with session.begin_nested():
    new_person = Person(name='Marylin', age=33)
    session.add(new_person)
    session.flush()

try:
    # this will fail and both will roll back
    with session.begin_nested():
        new_person_1 = Person(name='Phoebe', age=55)
        session.add(new_person_1)
        new_person_2 = Person(name='Phoebe', age=29)
        session.add(new_person_2)
except:
    print('Failed to insert two Phoebes!')

session.commit()
# at this point, there are no Phoebes and one Marylin in the DB :)
