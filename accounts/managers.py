from django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import ugettext_lazy as 

class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, number, password = None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        print(number)
        if not number:
            raise ValueError(('The number must be set'))
        # number = self.normalize_number(number)
        user = self.model(number=number, **extra_fields)
        user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self, number, password, **extra_fields):
        """
        Create and save a SuperUser with the given number and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(number, password, **extra_fields)