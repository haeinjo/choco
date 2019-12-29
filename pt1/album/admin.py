from django.contrib import admin
from .models import AlbumOwn, AlbumCovered

# Register your models here.


class AlbumOwnAdmin(admin.ModelAdmin):
    list_display = ('albumName',)

admin.site.register(AlbumOwn, AlbumOwnAdmin)


class AlbumCoveredAdmin(admin.ModelAdmin):
    list_display = ('albumName',)

admin.site.register(AlbumCovered, AlbumCoveredAdmin)