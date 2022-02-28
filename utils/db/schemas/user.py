from sqlalchemy import Column, Integer, Float
from utils.db.db_gino import db


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    longitude = Column(Float())
    latitude = Column(Float())

