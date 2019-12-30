from django.db import models

# Create your models here.
class SongOwn(models.Model):
    """
    date: 2019 - 12 - 10
    madeby: haein
    des: 자작곡
    """
    album = models.ForeignKey('album.AlbumOwn', null=True, on_delete=models.CASCADE, verbose_name='앨범')
    user = models.ForeignKey('user.CUser', null=True, on_delete=models.CASCADE, verbose_name='사용자')
    title = models.CharField(max_length=128, verbose_name="노래제목")
    composer = models.CharField(max_length=64, verbose_name="작곡가")
    lyricist = models.CharField(max_length=64, verbose_name="작사가")
    vocal = models.CharField(max_length=64, verbose_name="가수")
    genre = models.CharField(max_length=32, verbose_name="장르",\
    # choices=(
    #     ('', ''),
    # ))
    )
    lyrics = models.TextField(verbose_name="가사")
    comment = models.TextField(verbose_name="평가")
    bucketName = models.CharField(max_length=128, verbose_name="버킷이름")
    key = models.CharField(max_length=128, verbose_name="파일 이름")
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="등록날짜")

    def __str__(self):
        return '{} - {}'.format(str(self.vocal), str(self.title))

    class Meta:
        db_table = 'song_own'
        verbose_name = '자작곡'
        verbose_name_plural = '자작곡'


class SongCovered(models.Model):
    """
    date: 2019 - 12 - 10
    madeby: haein
    des: 커버곡
    """
    album = models.ForeignKey('album.AlbumCovered', null=True, on_delete=models.CASCADE, verbose_name='앨범')
    user = models.ForeignKey('user.CUser', null=True, on_delete=models.CASCADE, verbose_name='사용자')
    title = models.CharField(max_length=128, verbose_name="노래제목")
    vocal = models.CharField(max_length=64, verbose_name="가수")
    vocal_origin = models.CharField(max_length=64, verbose_name="원곡 가수")
    lyrics = models.TextField(verbose_name="가사")
    comment = models.TextField(verbose_name="평가")
    genre = models.CharField(max_length=32, verbose_name="장르")
    bucketName = models.CharField(max_length=128, verbose_name="버킷이름")
    key = models.CharField(max_length=128, verbose_name="파일 이름")   
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="등록날짜")

    def __str__(self):
        return '{} - {}'.format(self.vocal, self.title)

    class Meta:
        db_table = 'song_covered'
        verbose_name = '커버곡'
        verbose_name_plural = '커버곡'