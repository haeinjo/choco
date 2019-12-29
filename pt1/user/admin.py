from django.contrib import admin
from .models import CUser

# Register your models here.


class CUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')

admin.site.register(CUser, CUserAdmin)