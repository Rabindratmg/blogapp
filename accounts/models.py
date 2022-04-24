from audioop import maxpp
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=60)
    contact = models.CharField(max_length=10)
    bio = models.CharField(max_length=255)
        
    def __str__(self):
        return str(self.user)



@receiver(post_save, sender=User)
def create_profile(sender, instance, created,  **kwargs):

    if created:
        Profile.objects.create(user=instance)