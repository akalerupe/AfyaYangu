from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save


def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(person_of=instance)
        print("Profile successfully created")

post_save.connect(create_profile,sender=User)
