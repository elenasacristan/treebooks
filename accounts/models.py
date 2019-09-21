from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    '''extending the user Model using a OneToOneField'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_img = models.ImageField(upload_to='images', default="images/default_profile.png")
    subscribe = models.BooleanField(blank=False, default=False)
    test = models.CharField(max_length=15, default='testdefault')

    def __str__(self):
        return self.user.username

# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()