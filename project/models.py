from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(Text)
    user = Column(Integer, ForeignKey("user.id"))

    def __init__(self, task, user):
        self.task = task
        self.user = user.id

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(Text)
    name = Column(Text)
    
    def __init__(self, email, name):
        self.email = email
        self.name = name
