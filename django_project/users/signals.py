from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User) # okine se za save Usera
def createProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User) 
def saveProfile(sender, instance, created, **kwargs):
    instance.profile.save() # kad se sacuva user cuva se i profil