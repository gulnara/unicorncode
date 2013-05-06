import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, types
from sqlalchemy import Column, Integer,Text, String, DateTime, Date
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
import datetime

db_uri = os.environ.get('DATABASE_URL',"postgresql://localhost/tutorials" )
# engine = create_engine("sqlite:///tutorials.db", echo=False)

engine = create_engine(db_uri, echo=False)
session = scoped_session(sessionmaker(bind=engine, autocommit = False, autoflush = False))


Base = declarative_base()
Base.query = session.query_property()


### Class declarations

class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key = True)
	email = Column(String(64), nullable = True)
	password = Column(String(64), nullable = True)


class Tutorial(Base):
	__tablename__ = "tutorials"

	id = Column(Integer, primary_key = True)
	user_id = Column(Integer, ForeignKey('users.id'))
	title = Column(Text, nullable = True)
	tutorial = Column(Text, nullable = True)

	user = relationship("User", backref=backref("tutorials", order_by = id))
	

### End class declarations


def main():
    """In case we need this for something"""
    pass


if __name__ == "__main__":
    main()