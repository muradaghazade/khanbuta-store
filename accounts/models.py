from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, UnicodeUsernameValidator
from products.common import slugify
from .managers import UserManager
from django.contrib.auth.base_user import BaseUserManager
import random


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
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = 'Istifadeci'
        verbose_name_plural = 'Istifadeciler'

    def __str__(self):
        return f"{self.number}"


class OTPCode(models.Model):
    code = models.CharField(max_length=6, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_index=True, related_name='code')

    class Meta:
        verbose_name = 'OTP Kod'
        verbose_name_plural = 'OTP Kodlar'

    def __str__(self):
        return f"{self.code}" 

    def save(self, *args, **kwargs):
        num_list = [i for i in range(10)]
        code_items = []

        for i in range(6):
            num = random.choice(num_list)
            code_items.append(num)

        code = "".join(str(item) for item in code_items)
        self.code = code
        super(OTPCode, self).save(*args, **kwargs)

    