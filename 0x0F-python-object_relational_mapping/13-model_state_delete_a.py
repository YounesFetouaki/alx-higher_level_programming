#!/usr/bin/python3

""" Module that deletes all State objects with a name containing the letter
'a' from the database hbtn_0e_6_usa """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def delete_states():
    """ Deletes all State objects with a name containing the letter 'a' from
    the database hbtn_0e_6_usa """

    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter(State.name.contains('a')):
        session.delete(state)
    session.commit()
    session.close()


if __name__ == '__main__':
    delete_states()
