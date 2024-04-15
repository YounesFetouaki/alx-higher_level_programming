#!/usr/bin/python3

""" Module that lists all State objects
from the database hbtn_0e_6_usa """

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def update_state():
    """ Function that lists all State objects
    from the database hbtn_0e_6_usa """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()

    session.close()


if __name__ == "__main__":
    update_state()
