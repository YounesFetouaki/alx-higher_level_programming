#!/usr/bin/python3

""" Module that prints all City objects from the database hbtn_0e_14_usa """


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_cities():
    """ Prints all City objects from the database hbtn_0e_14_usa """

    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state in session.query(City, State).\
            filter(City.state_id == State.id).order_by(City.id):
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()


if __name__ == '__main__':
    print_cities()
