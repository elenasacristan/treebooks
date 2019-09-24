'''
I have created the userprofile app following the steps in the following tutorial
https://www.youtube.com/watch?v=qLRxkStiaUg
'''

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):

    '''extending the user Model using a OneToOneField'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_img = models.ImageField(upload_to='images', default="images/default_profile.png", blank=True)
    subscribe = models.BooleanField(blank=True, default=False)
    bio = models.TextField(blank=True)
    dob = models.DateField(null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    contact_by_phone = models.BooleanField(blank=True, default=False)
    contact_by_email = models.BooleanField(blank=True, default=False)


    def __str__(self):
        return self.user.username   

'''
With the code below we are saying that the user has a profile property
Whenever we pass a user object to this property it will trigger the UserProfile
run through its objects and fire off the get or create method.
And what this does is.. if this object is in the database get this object and
should return the user object and if it is not in the databse it should create one
'''
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0]) 