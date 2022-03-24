from django.contrib import admin
from accounts.models import *

admin.site.register([User, OTPCode, City, Region, Avenue, Street, SocialIcon, SocialMedia, UserCategory])
