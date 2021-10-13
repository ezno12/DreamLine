#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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
