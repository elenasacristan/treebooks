from django.test import TestCase
from .models import UserProfile
from django.contrib.auth.models import User


class TestUserReviewModels(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="username", password="password1234")
    
    def test_can_create_profile(self):
        userprofile = UserProfile(
            user = self.user,
            profile_img = None,
            subscribe = False,
            dob = '01-01-2000',
            telephone = '',
            contact_by_phone = False,
            contact_by_email = False,
        )
        self.assertEqual(userprofile.user.username, 'username')
        self.assertEqual("username", str(userprofile))
