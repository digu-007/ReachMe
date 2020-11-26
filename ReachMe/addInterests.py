from django.db import models
from django.contrib.auth.models import User

from user.models import *

""" To execute this file, run command: python manage.py shell < addInterests.py """

listOfInterests = ["ty", "yep", "go"]

def Add(cur):
    cur = Interest(name=cur)
    cur.save()

for curInterest in listOfInterests:
    Add(curInterest)
