from django.db import models


class Tag(models.Model):
    """
    date: 2019 - 12 - 13
    madeby: haein
    des: 평가 - 태그
    """
    content = models.CharField(max_length=32, verbose_name="태그")
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="등록날짜")

    def __str__(self):
        return self.content
    
    class Meta:
        db_table = 'tag'
        verbose_name = "태그"
        verbose_name_plural = "태그"


class 