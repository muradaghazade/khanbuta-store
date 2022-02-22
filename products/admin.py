from django.contrib import admin
from .models import *

admin.site.register([Logo, Category, HeaderText, SubCategory, SubSubCategory, Filter, CategoryLine, Slider, Benefit, DisplayedCategory, Product, Partner, Image, FilterValue, Tag, AboutUs, AboutUsService, AboutUsCarousel, FAQCategory, FAQ, Rating, DiscountProduct])