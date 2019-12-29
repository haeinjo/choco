from django.db import models


class Tag(models.Model):
    """
    date: 2019 - 12 - 13
    madeby: haein
    des: 태그
    """
    content = models.CharField(max_length=32, verbose_name="태그")
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="등록날짜")

    def __str__(self):
        return self.content
    
    class Meta:
        db_table = 'tag'
        verbose_name = "태그"
        verbose_name_plural = "태그"


class SongOwnTag(models.Model):
    """
    date: 2019 - 12 - 13
    madeby: haein
    des: 자작곡 - 태그(Many To Many)
    """
    song = models.ForeignKey('song.SongOwn', on_delete=models.CASCADE, verbose_name="자작곡")
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, verbose_name="태그")
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    def __str__(self):
        return str(self.song) + "-" + str(self.tag)

    class Meta:
        db_table = 'song_own_tag'
        verbose_name = '자작곡 - 태그'
        verbose_name_plural = '자작곡 - 태그'


class SongCoveredTag(models.Model):
    """
    date: 2019 - 12 - 13
    madeby: haein
    des: 커버곡 - 태그(Many To Many)
    """
    song = models.ForeignKey('song.SongCovered', on_delete=models.CASCADE, verbose_name="커버곡")
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, verbose_name="태그")

    def __str__(self):
        return str(self.song) + "-" + str(self.tag)

    class Meta:
        db_table = 'song_covered_tag'
        verbose_name = '커버곡 - 태그'
        verbose_name_plural = '커버곡 - 태그'


