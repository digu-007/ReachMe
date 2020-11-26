from django.db import models
from django.contrib.auth.models import User


class Interest(models.Model):
    name = models.CharField(max_length=127, null=True, unique=True)

    def __str__(self):
        return self.name

class UserInfo(models.Model):
    GENDER_OPTIONS = (
                    ('Male', 'Male'),
                    ('Female', 'Female'),
                    ('Transgender', 'Transgender'),
    )

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=127, null=True)
    phone = models.CharField(max_length=31, null=True)
    profile_pic = models.ImageField(null=True, blank = True)
    date_of_birth = models.DateField(max_length=8, null=True)
    gender = models.CharField(max_length=15, null=True, blank=True, choices=GENDER_OPTIONS)
    interests = models.ManyToManyField(Interest)
    # location =

    def __str__(self):
        return self.name
