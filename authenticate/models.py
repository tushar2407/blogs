from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name=models.CharField(max_length=256)
    last_name=models.CharField(max_length=256)
    email=models.EmailField()
    birth_date=models.DateTimeField(null=True)
    def __str__(self):
        return self.user.username
@receiver(post_save,sender=User)
def update_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()