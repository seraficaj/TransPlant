
#import datetime for review posts
import datetime


from flask_login import UserMixin
from flask_bcrypt import generate_password_hash

#import peewee ORM
from peewee import * 

#set Database 
DATABASE = SqliteDatabase('PlantSwipe.db')

#review Model
class Review(Model):
  plant = TextField() 
  user = TextField()
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



class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=50)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)

    class Meta:
        database = DATABASE  
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
            
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Review, Plant], safe=True)
    DATABASE.close()

