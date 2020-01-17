from django.contrib import admin
from .models import SongOwn, SongCovered, SongRecommended

# Register your models here.


class SongOwnAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'composer', 'lyricist')

admin.site.register(SongOwn, SongOwnAdmin)


class SongCoveredAdmin(admin.ModelAdmin):
    list_display = ('title', 'vocal_origin', 'genre', 'vocal')

admin.site.register(SongCovered, SongCoveredAdmin)

class SongRecommendedAdmin(admin.ModelAdmin):
    model = SongRecommended
    list_display = ('songOwn', 'songCovered', 'register_date')
    # list_display = ('get_title', 'get_title2', 'register_date')

    # def get_title(self, obj):
    #     return obj.songOwn.title
    # def get_title2(self, obj):
    #     return obj.songCovered.title
    # get_title.short_description = '추천 자작곡'
    # get_title2.short_description = '추천 커버곡'

admin.site.register(SongRecommended, SongRecommendedAdmin)