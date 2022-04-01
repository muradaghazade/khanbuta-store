from django.contrib import admin
from .models import *

admin.site.register([Logo, Category, HeaderText, SubCategory, SubSubCategory, Filter, CategoryLine, Slider, Benefit, DisplayedCategory, Partner, Image, FilterValue, Tag, AboutUs, AboutUsService, AboutUsCarousel, FAQCategory, FAQ, Rating, DiscountProduct, Wishlist, ProductVersion, Cart, CategoryBanner, Number, StoreOrder, Order, SocialLink, CategoryReklam])

class ProductImageInline(admin.TabularInline):
    model = Image

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    raw_id_fields = ['user']


admin.site.register(Product, ProductAdmin)