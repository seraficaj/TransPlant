import datetime
from peewee import *


  # We use the built in SqliteDatabase() function from peewee 
  # to save a reference to a DB file to a DATABASE variable
DATABASE = SqliteDatabase('plant_api.db')

class Plant(Model):
    image = CharField()
    species = CharField()
    watering = IntegerField()
    light = IntegerField()
    difficulty = IntegerField()

    class Meta:
        database = DATABASE
        # order_by = ('-timestamp')

class User(Model):
    name: CharField()
    email: CharField()
    password: CharField()

def initialize():
  DATABASE.connect()
  DATABASE.create_tables([Plant, User], safe=True)
  DATABASE.close()