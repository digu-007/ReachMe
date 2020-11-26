from django.db import models
from django.contrib.auth.models import User

from user.models import *

""" To execute this file, run command: python manage.py shell < addInterests.py """

listOfInterests = ["ty", "tf", "yep"]

def Add(curInterest):
    cur = Interest(name=curInterest)
    cur.save()

def Work():
    for curInterest in listOfInterests:
        Add(curInterest)

Work()
