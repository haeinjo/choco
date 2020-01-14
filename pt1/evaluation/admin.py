from django.contrib import admin
from .models import Tag, SongOwnTag, SongCoveredTag, ScoreOwn, ScoreCovered

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


class ScoreOwnAdmin(admin.ModelAdmin):
    model = ScoreOwn
    list_display = ('get_title', 'score')

    def get_title(self, obj):
        return obj.song.title
    get_title.short_description = '자작곡'

admin.site.register(ScoreOwn, ScoreOwnAdmin)


class ScoreCoveredAdmin(admin.ModelAdmin):
    model = ScoreCovered
    list_display = ('get_title', 'score')

    def get_title(self, obj):
        return obj.song.title
    get_title.short_description = '커버곡'

admin.site.register(ScoreCovered, ScoreOwnAdmin)