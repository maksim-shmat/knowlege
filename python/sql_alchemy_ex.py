"""SQL Alchemy about."""

#1

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
        Column, Integer, String, ForeignKey, create_engine)
from sqlalchemy.orm import relationship


engine = create_engine('sqlite:///:memory:')
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    addresses = relationship(
            'Address',
            back_populates='person',
            order_by='Address.email',
            cascade='all, delete-orphan'
    )

    def __repr__(self):
        return f'{self.name}(id={self.id})'


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship('Person', back_populates='addresses')

    def __str__(self):
        return self.email
    __repr__ = __str__

Base.metadata.create_all(engine)

#1.1 it for diff file

from alchemy_models import Person, Address, engine
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()

anakin = Person(name='Anakin Skywalker', age=32)
obi1 = Person(name='Obi-Wan Kenobi', age=40)

obi1.addresses = [
        Address(email='obi1@example.com'),
        Address(email='wanwan@example.com'),
]
anakin.addresses.append(Address(email='ani@example.com'))
anakin.addresses.append(Address(email='evil.dart@example.com'))
anakin.addresses.append(Address(email='vader@example.com'))

session.add(anakin)
session.add(obi1)
session.commit()

#1.2 results manipulations

obi1 = session.query(Person).filter(
        Person.name.like('Obi%')
).first()
print(obi1, obi1.addresses)

###

anakin = session.query(Person).filter(
        Person.name=='Anakin Skywalker').first()
print(anakin, anakin.addresses)

###

anakin_id = anakin.in
del anakin

###

def display_info():
    # get all addresses first
    addresses = session.query(Address).all()

    # display results
    for address in addresses:
        print(f'{address.person.name} <{address.email}>')

    # display how many objects we have in total
    print('people: {}, addresses: {}'.format(
        session.query(Person).count(),
        session.query(Address).count())
    )

### check func display_info()

display_info()

anakin = session.query(Person).get(anakin_id)
session.delete(anakin)
session.commit()

display_info()

###
