from django.contrib import admin
from .models import SongOwn, SongCovered

# Register your models here.


class SongOwnAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'composer', 'lyricist')

admin.site.register(SongOwn, SongOwnAdmin)


class SongCoveredAdmin(admin.ModelAdmin):
    list_display = ('title', 'vocal_origin', 'genre', 'vocal')

admin.site.register(SongCovered, SongCoveredAdmin)