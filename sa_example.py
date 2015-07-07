from __future__ import print_function

from sqlalchemy import Column, Integer, String
from sa_common import Base, session


class Person(Base):
    __tablename__ = 'persons'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)


persons = session.query(Person).filter(Person.name > 'Leonardo').order_by(Person.name)

for person in persons:
    print(person.name)
