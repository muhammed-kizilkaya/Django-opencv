from django.contrib import admin
from .models import UserEntry 
# Register your models here.

class UserEntryAdmin(admin.ModelAdmin):
    list_display = (  'header', 'description', 'created_date', 'rating')

admin.site.register(UserEntry, UserEntryAdmin)