from django.contrib import admin

from app.models import CustomUser


# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id', 'user_name', 'user_social_id', 'email_address', 'contact_number', 'registered_date',
        'account_suspended')
    search_fields = ('user_name', 'email_address', 'user_social_id')
    list_filter = ('account_suspended', 'account_deleted', 'registered_date')
