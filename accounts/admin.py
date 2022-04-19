from django.contrib import admin
from accounts.models import *

admin.site.register([OTPCode, City, Region, Avenue, Street, SocialIcon, SocialMedia, UserCategory])

class UserAdmin(admin.ModelAdmin):
    list_display = ('number', 'is_vendor', 'is_verified_by_admin')
    # readonly_fields = ('membership_id',)
    # ordering = ('-id',)
    search_fields = ('email', 'number', 'name', 'first_name', 'last_name')

admin.site.register(User, UserAdmin)


admin.site.site_header = "Ipekyolu"
admin.site.index_title = "Ipekyolu"
admin.site.site_title = "Ipekyolu Administration"