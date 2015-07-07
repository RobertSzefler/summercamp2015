from __future__ import print_function

from sqlalchemy import Column, Integer, String
from sa_common import Base, session


class Person(Base):
    __tablename__ = 'persons'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)


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
