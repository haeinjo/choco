from django.contrib import admin
from .models import Tag, SongOwnTag, SongCoveredTag

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_display = ('content',)

admin.site.register(Tag, TagAdmin)


class SongOwnTagAdmin(admin.ModelAdmin):
    list_display = ('song', 'tag')

admin.site.register(SongOwnTag, SongOwnTagAdmin)


class SongCoveredTagAdmin(admin.ModelAdmin):
    list_display = ('song', 'tag')

admin.site.register(SongCoveredTag, SongCoveredTagAdmin)