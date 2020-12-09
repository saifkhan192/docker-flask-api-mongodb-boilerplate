from flask_app import db, mongodb as mongome, declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType, func, text, Enum
from sqlalchemy.orm import sessionmaker
from mongoengine.queryset import queryset_manager
from mongoengine.queryset.visitor import Q


Base = declarative_base()


class User(Base):
    """Data model for user accounts."""

    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = Column(db.Integer,
                primary_key=True)
    username = Column(String(64),
                      unique=True,
                      nullable=False)
    email = Column(String(80),
                   index=True,
                   nullable=False)
    created = Column(DateTime,
                     nullable=False,
                     server_default=text("CURRENT_TIMESTAMP"))
    bio = Column(Text,
                 nullable=True)
    admin = Column(Boolean,
                   nullable=False,
                   server_default=text("0"))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Subscriber(Base):
    __tablename__ = 'subscribers'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    email = Column(String(80), nullable=False, unique=True)
    created = Column(DateTime, nullable=False,
                     server_default=text("CURRENT_TIMESTAMP"))

    def serialize(self):
        return {"id": self.id,
                "name": self.email,
                "name": self.created}
# class Post(Document):
#     title = StringField(required=True, max_length=200)
#     content = StringField(required=True)
#     author = StringField(required=True, max_length=50)
#     published = DateTimeField(default=datetime.datetime.now)
