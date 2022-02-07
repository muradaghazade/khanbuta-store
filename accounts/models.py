from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, UnicodeUsernameValidator
from products.common import slugify
from .managers import UserManager
from django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator
    username = models.CharField(
        ('username'),
        max_length=150,
        blank=True,
        null=True,
        unique=False,
        help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    email = models.EmailField(('email adress'), unique=True, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    number = models.CharField(('Number'),max_length=100, unique=True, null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    password2 = models.CharField(('password2'), max_length=200, editable=False)

    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.number}"

    # def save(self, *args, **kwargs):
    #     super(User, self).save(*args, **kwargs)
    #     self.slug = f'{slugify(self.number)}-{self.id}'
    #     super(User, self).save(*args, **kwargs)
