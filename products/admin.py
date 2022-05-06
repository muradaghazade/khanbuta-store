from django.contrib import admin
from .models import *

admin.site.register([Logo, Category, HeaderText, Filter, CategoryLine, Slider, Benefit, DisplayedCategory, Partner, Image, FilterValue, Tag, AboutUs, AboutUsService, AboutUsCarousel, FAQCategory, FAQ, Rating, DiscountProduct, Wishlist, ProductVersion, Cart, CategoryBanner, Number, StoreOrder, Order, SocialLink, CategoryReklam])

class ProductImageInline(admin.TabularInline):
    model = Image

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    raw_id_fields = ['user']

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title','get_category')
    def get_category(self, obj):
        return obj.category.title
    get_category.short_description = 'category'

class SubSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title','get_category')
    def get_category(self, obj):
        return obj.category.title
    get_category.short_description = 'subCategory'

admin.site.register(Product, ProductAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(SubSubCategory, SubSubCategoryAdmin)