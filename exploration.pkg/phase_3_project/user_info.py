from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __init__(self, username, password):
         self.username = username
         self.password = password

    def __repr__(self):
        return f"<User, username: {self.username} password: {self.password}>" 

if __name__ == '__main__':
        Base.metadata.create_all(engine)

        user1 = User(username='flat', password='iron')
        session.add(user1)
        session.commit()
        session.close()