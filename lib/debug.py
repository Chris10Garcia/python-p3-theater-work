#!/usr/bin/env python3


from sqlalchemy import create_engine, desc, func
from sqlalchemy.orm import sessionmaker
from faker import Faker

from models import Audition, Role

if __name__ == '__main__':
    engine = create_engine('sqlite:///threater_work.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()