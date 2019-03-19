#import datetime for review posts
import datetime

#import peewee ORM
from peewee import * 

#set Database 
DATABASE = SqliteDatabase("PlantSwipe.db")

#review Model
class Review(Model):
  plant: TextField() 
  user: TextField()
  rating: IntegerField()
  text: TextField()
  timestamp: DateTimeField(default=datetime.datetime.now)

  class Meta:
    database = DATABASE
    order_by = ('-timestamp',)

#plant Model
class Plant(Model):
  image: CharField()
  species: CharField()
  watering: IntegerField()
  Light: IntegerField()
  Difficulty: IntegerField()

  class Meta:
    database = DATABASE


def initialize():
  DATABASE.connect()
  DATABASE.create_tables([Review,Plant], safe=True)
  DATABASE.close()