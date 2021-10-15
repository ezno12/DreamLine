#!/usr/bin/python3
import sys
from sqlalchemy import Column, String, Integer, sqlalchemy, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.orm import relationship
from datetime import date, datetime
from sqlalchemy.orm import sessionmaker

"""
#Data base creation
"""


""" user will inherit of declarative_base by default to start making tables
    and an instance Base = declarative_base()
"""

Base = declarative_base()
# base class contains a MetaData object where newly
# defined Table objects are collected.

class user(Base):
# creation user table
    __tablename__ = "user"
    id = (Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column('Username',String(20), nullable=False)
    password = Column('Password',String(256), nullable=False)
    first_name = Column('First Name', String(15), nullable = False)
    last_name = Column('Last Name', String(15), nullable = False) 
    period = 
# It allows you to access the linked records as a list with something like Parent.
# cascade option makes the parent child changes to change together
    todo = relationship("todo",uselist = True, back_populates= "user", cascade = "all")

class todo(Base):
    """ class define the todo table
    """
    # creation todo table
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column('Task Name',String(256), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'),autoincrement=True, nullable=False)
    date_created = Column(datetime.utcnow, Date)



if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # CREATE statements for all tables:
    user.metadata.create_all(engine)
    todo.metadata.create_all(engine)
    print("<%r> <%r>".metadata.create_all(engine).format(user,todo))


"""
#Data Base sessions
"""


if __name__ == '__main__':
    # connect to the DB
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # Access the tables (like cursor)
    Base.metadata.create_all(engine)
    # talk to the DB: usning sessions

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    mySession = Session()



    # use variables here


    """
    cursor = db.cursor()
    ### sql query string to be executed on the database
    sql = """#SELECT cities.id, cities.name, states.name
            #FROM cities
            #JOIN states
            #ON states.id = cities.state_id
            #ORDER BY cities.id
            """
    ### Execute the SQL command
    cursor.execute(sql)
    ### Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    ### Now print fetched result
    for row in results:
        print(row)
    cursor.close()
    db.close()
    
    """

