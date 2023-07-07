#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Audition, Role

engine = create_engine('sqlite:///threater_work.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

def delete_records():
    session.query(Audition).delete()
    session.query(Role).delete()
    session.commit()

def create_records():
    roles = [Role(character_name = fake.first_name()) for i in range(50)]

    auditions = [Audition(
                actor = fake.name(),
                location = fake.city(),
                phone = fake.phone_number(),
                hired = False,
                role_id = None,
                ) for i in range(500)]
    
    session.add_all(roles + auditions)
    session.commit()
    return roles, auditions

def relate_records(roles, auditions):
    for audition in auditions:
        audition.role_id = random.randint(1, len(roles))
    
    session.add_all(auditions)
    session.commit()

if __name__ == '__main__':
    delete_records()
    roles, auditions = create_records()
    relate_records(roles, auditions)