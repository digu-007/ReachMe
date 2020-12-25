from django.db import models
from django.contrib.auth.models import User

from user.models import *

listOfInterests = [
    "Coding",
    "Basketball",
    "Running",
    "Cooking",
    "Video Games",
    "Trekking",
    "Dancing",
    "Sleeping"
]

"""
Chirag Thakur
Digvijay Janartha
Rohit Sharma
Abhimanyu Singh
Rohit Mehta
Mannat Kapil
Lakshay Gupta
Rohit Kumar
Mukul Koundal
Apresh Koundal
"""

def Add(curInterest):
    cur = Interest(name=curInterest)
    cur.save()

def Work():
    for curInterest in listOfInterests:
        Add(curInterest)

Work()
