from django.db import models

# Create your models here.

class AlbumOwn(models.Model):
    """
    date: 2019 - 12 - 10
    madeby: haein
    des: 앨범 - 자작곡
    """
    albumName = models.CharField(max_length=256, none=True, verbose_name='앨범이름')
    img_path = models.CharField(max_length=512, none=True, verbose_name="커버사진경로")
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="발매일")

    def __str__(self):
        return self.albumName

    class Meta:
        db_table = 'albom_own'
        verbose_name = '자작곡 앨범'
        verbose_name_plural = '자작곡 앨범'


class AlbumCovered(models.Model):
    """
    date: 2019 - 12 - 10
    madeby: haein
    des: 앨범 - 커버곡
    """
    albumName = models.CharField(max_length=256, none=True, verbose_name='앨범이름')
    img_path = models.CharField(max_length=512, none=True, verbose_name="커버사진경로")
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="발매일")

    def __str__(self):
        return self.albumName

    class Meta:
        db_table = 'albom_covered'
        verbose_name = '커버곡 앨범'
        verbose_name_plural = '커버곡 앨범'