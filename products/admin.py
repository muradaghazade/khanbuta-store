from django.contrib import admin
from .models import *

admin.site.register([Logo, Category, HeaderText, SubCategory, SubSubCategory])