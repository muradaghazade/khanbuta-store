from django.contrib import admin
from accounts.models import User, OTPCode

admin.site.register([User, OTPCode,])
