from django.contrib.auth.models import User

# Authenticate a user by exact match on email and password
class EmailAuth:
    
    def authenticate(self, username=None, password=None):
        """
        Get an instance of the User based off the email 
        and the verified password
        """
        try:
             """ username is used because it is the
            name in the form
             """
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user
            
            return None
        
        except User.DoesNotExist:
            return None
        

    def get_user(self, user_id):
        """
        Used by the Django authentiation system to retrieve 
        a user instance
        """
        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user
            
            return None

        except User.DoesNotExist:
            return None