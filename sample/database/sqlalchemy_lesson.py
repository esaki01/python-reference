import sqlalchemy.ext.declarative
import sqlalchemy.orm

engine = sqlalchemy.create_engine('sqlite:///sqlalchemy_lesson.db', echo=True)
Base = sqlalchemy.ext.declarative.declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))


Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

# インサートする
person1 = Person(name='Mike')
session.add(person1)
person2 = Person(name='Nancy')
session.add(person2)
person3 = Person(name='Jun')
session.add(person3)
session.commit()

# セレクトする
person4 = session.query(Person).filter_by(name='Mike').first()

# アップデートする
person4.name = 'Michel'
session.add(person4)
session.commit()

# セレクトする
person5 = session.query(Person).filter_by(name='Nancy').first()

# デリートする
session.delete(person5)
session.commit()

# セレクトオールする
persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)
