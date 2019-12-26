from django.db import models

# Create your models here.

class CUser(models.Model):
    """
    date: 2019 - 12 - 10
    madeby: haein
    des: 사용자
    """
    name = models.CharField(max_length=64, verbose_name="이름")
    email = models.EmailField(max_length=128, verbose_name='이메일')
    phone = models.CharField(max_length=128, verbose_name='휴대폰 번호')

    def __str__(self):
        return str(self.name) + ' - ' + str(self.phone)

    class Meta:
        db_table = 'user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'