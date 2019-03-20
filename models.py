
#import datetime for review posts
import datetime

import json

from flask_login import UserMixin
from flask_bcrypt import generate_password_hash

#import peewee ORM
from peewee import * 

#set Database 
DATABASE = SqliteDatabase('PlantSwipe.db')

class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=50)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)

    class Meta:
        database = DATABASE  
        
    def get_plants(self):
        return userPlants.select().where(userPlants.user == self)
        
    def get_stream(self):
        return userPlants.select().where(userPlants.user == self)
 

    @classmethod
    def create_user(cls, username, email, password, admin=False):
        try:
            cls.create(
                username=username,
                email=email,
                password=generate_password_hash(password),
                is_admin=admin)
        except IntegrityError:
            raise ValueError("User already exists")

#review Model
class Review(Model):
  plant = TextField() 
  rating = IntegerField()
  text = TextField()
  timestamp = DateTimeField(default=datetime.datetime.now)

  class Meta:
    database = DATABASE
    order_by = ('-timestamp',)


#plant Model
class Plant(Model):
  image = CharField()
  species = CharField()
  watering = IntegerField()
  light = IntegerField()
  Difficulty =  IntegerField()

  class Meta:
    database = DATABASE

class userPlants(Model):
  user = ForeignKeyField(
      model = User,
      backref= 'swipe'
  )
  content = TextField()
  class Meta:
    database = DATABASE
    

   



            
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Review, Plant, userPlants], safe=True)
    DATABASE.close()

