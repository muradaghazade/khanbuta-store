from unicodedata import category
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
    name = models.CharField(max_length=100, null=True, blank=True)
    number = models.CharField(('Number'),max_length=100, unique=True, null=True, blank=True)
    # address = models.CharField(max_length=3000, null=True, blank=True)
    address_addtional = models.CharField(max_length=300, null=True, blank=True)
    cover_image = models.ImageField('Image',upload_to='images/', null=True, blank=True)
    logo = models.ImageField('Image',upload_to='images/', null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    password2 = models.CharField(('password2'), max_length=200, editable=False)
    category = models.ForeignKey('UserCategory', on_delete=models.CASCADE, related_name='users', blank=True, null=True)
    sub_category = models.ForeignKey('UserSubCategory', on_delete=models.CASCADE, related_name='users', blank=True, null=True)
    sub_sub_category = models.ForeignKey('UserSubSubCategory', on_delete=models.CASCADE, related_name='users', blank=True, null=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, related_name='users', blank=True, null=True)
    region = models.ForeignKey('Region', on_delete=models.CASCADE, related_name='users', blank=True, null=True)
    avenue = models.ForeignKey('Avenue', on_delete=models.CASCADE, related_name='users', blank=True, null=True)
    street = models.ForeignKey('Street', on_delete=models.CASCADE, related_name='users', blank=True, null=True)
    rating = models.PositiveSmallIntegerField('rating', null=True, blank=True)
    is_verified_by_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False, editable=False)
    is_vendor = models.BooleanField(default=False)
    is_store = models.BooleanField(default=False)

    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = 'Istifadeci'
        verbose_name_plural = 'Istifadeciler'

    def __str__(self):
        if self.is_vendor == True:
            return f"{self.name}"
        else:
            return f"{self.number}"


class UserCategory(models.Model):
    title = models.CharField(max_length=200, unique=True)
    icon = models.ImageField('Image',upload_to='icons/', null=False, blank=False)
    slug = models.SlugField(max_length=200, null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(UserCategory, self).save(*args, **kwargs)
        self.slug = slugify(self.title)
        super(UserCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'
        ordering = ['title']


class UserSubCategory(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(UserCategory, on_delete=models.CASCADE, related_name='sub_categories', blank=True, null=True)
    # parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=200, editable=False, null=True)
    icon = models.ImageField('Icon',upload_to='icons/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Alt kateqoriya"
        verbose_name_plural = "Alt kateqoriyalar"
        ordering = ['title']

    def save(self, *args, **kwargs):
        super(UserSubCategory, self).save(*args, **kwargs)
        self.slug = slugify(self.title)
        super(UserSubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class UserSubSubCategory(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(UserSubCategory, on_delete=models.CASCADE, related_name='sub_sub_categories', blank=True, null=True)
    # parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=200, editable=False, null=True)
    icon = models.ImageField('Icon',upload_to='icons/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Alt Alt kateqoriya"
        verbose_name_plural = "Alt Alt kateqoriyalar"
        ordering = ['title']

    def save(self, *args, **kwargs):
        super(UserSubSubCategory, self).save(*args, **kwargs)
        self.slug = slugify(self.title)
        super(UserSubSubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


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

    
class City(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Sheher'
        verbose_name_plural = 'Sheherler'


class Region(models.Model):
    title = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='regions', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Rayon'
        verbose_name_plural = 'Rayonlar'


class Avenue(models.Model):
    title = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='avenues', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Qesebe'
        verbose_name_plural = 'Qesebeler'


class Street(models.Model):
    title = models.CharField(max_length=50)
    avenue = models.ForeignKey(Avenue, on_delete=models.CASCADE, related_name='streets', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kuce'
        verbose_name_plural = 'Kuceler'


class SocialMedia(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField('Logo',upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class SocialIcon(models.Model):
    url = models.CharField(max_length=1000)
    social_media = models.ForeignKey(SocialMedia, on_delete=models.CASCADE, related_name='social_icons', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='social_icons', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
