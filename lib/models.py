from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, Boolean
from sqlalchemy.orm import relationship, backref, Mapped
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Audition(Base):
    __tablename__ = "auditions"

    id = Column(Integer(), primary_key = True)
    actor = Column(String())
    location = Column(String())
    phone = Column(Integer())
    hired = Column(Boolean())

    role_id = Column(Integer(), ForeignKey('roles.id'))

    def __repr__(self):
        return f"Audition with {self.actor} at the {self.location}"
    
    def call_back(self):
        self.hired = True
        return f"{self.actor} has been hire for the role: {self.role.character_name}"


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer(), primary_key = True)
    character_name = Column(String())

    auditions = relationship('Audition', backref=backref('role'))

    def __repr__(self):
        return f"This is the role for {self.character_name}"

    # actors : Mapped[List["Audition"]] = relationship()

    #to call a method as a property, use the decorator @property
    @property #ASDKJA:LSDJA:SLDJAS:LJDKASD
    def actors(self):
        # it was this simple! i kept calling actors without (), which returned the function
        # tried searching within sqlalchemy docs to no avail
        # first search for <bound methods> was the correct source. shouldn't have been too
        # quick to dismiss this result
        return [audition.actor for audition in self.auditions]

    @property 
    def locations(self):
        return [audition.location for audition in self.auditions]
    
    def lead(self):
        hired = [audition for audition in self.auditions if audition.hired == 1]
        try:
            return hired[0]
        except:
            return 'No actor has been hired for this role.'
        
    def understudy(self):
        hired = [audition for audition in self.auditions if audition.hired == 1]
        try:
            return hired[1]
        except:
            return 'no actor has been hired for understudy for this role.'

# create the classes
#   auditions *done*
#   roles *done*

# establish relationships
#   roles = one *done*
#   audition = many *done*

# migrattion
#   run alembic init *done*
#   run alembic revision autogenerate *done*

# testing
#   create seed data *done*
#   test relationship methods  *done*

# create methods for auditions *done*
# create methods for roles *done*