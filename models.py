import sqlite3
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

engine = create_engine('sqlite:///users.db', echo=False)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname= Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f'<User, name:{self.name}, fullname:{self.fullname}, nickname:{self.nickname} >'


    def add_name(self, new_name):
        sql = f"""
        INSERT INTO users (name)
        VALUES ('{new_name}')
        """
        cursor.execute(sql)
        conn.commit()

    def delete_user(self, id):
        sql = f"""
        DELETE FROM users
        WHERE id = ?
        """    
        cursor.execute(sql, (id))
        conn.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)



# print('engine:', engine)
# print('create_engine:', create_engine)
# print('declarative_base:', declarative_base)
# print(sqlite3)
# print(User().add_name('Jack Hughes'))
print(User().delete_user('4'))