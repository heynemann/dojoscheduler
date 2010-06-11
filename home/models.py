from appengine_django.models import BaseModel
from google.appengine.ext import db

class Dojo(BaseModel):
    title = db.StringProperty()
    date = db.DateTimeProperty('dojo date')
    finished = db.BooleanProperty()

