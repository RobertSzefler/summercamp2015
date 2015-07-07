from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker


dsn = 'mysql://test:test@localhost/test'
engine = create_engine(dsn)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
