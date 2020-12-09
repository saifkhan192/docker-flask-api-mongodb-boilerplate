import os, datetime
from models.auth import *
from models.sqlacodegen_models import *
import models as m
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean, PickleType, func, text, Enum
from flask_app import app, mongodb, db, Base

# Base = declarative_base()

def _create_db_tables(dropFirst=True):
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from os import environ

    # Create engine
    db_uri = environ.get('SQLALCHEMY_DATABASE_URI')
    engine = create_engine(db_uri, echo=True)

    # Create All Tables
    # if dropFirst:
    # Base.metadata.drop_all(engine)
    print(Base.metadata.create_all(engine))
    # Session = sessionmaker(bind=engine)
    # session = Session()
    # print ( session.execute('SHOW CREATE TABLE subscribers').fetchone()[1] )
    # print ( session.execute('SHOW CREATE TABLE users').fetchone()[1] )
    # Accomodation().save()
    with app.app_context():
        db.session.add( Place(name="Swat",description="",status="published",loc_id=1) )
        db.session.commit()

def run_mysql_migrations():
	_create_db_tables(True)

run_mysql_migrations()