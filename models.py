from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname= Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f'<User, name:{self.name}, fullname:{self.fullname}, nickname:{self.nickname} >'

if __name__ == '__main__':
# Base.metadata.create_all(engine)
    jack_hughes_user = User(name='Jack Hughes', fullname='Yaakov Hughes', nickname='Silky Smooth Hughes')
    session.add(jack_hughes_user)
    session.commit()