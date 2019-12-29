# Generated by Django 3.0.1 on 2019-12-29 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('album', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongOwn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='노래제목')),
                ('composer', models.CharField(max_length=64, verbose_name='작곡가')),
                ('lyricist', models.CharField(max_length=64, verbose_name='작사가')),
                ('vocal', models.CharField(max_length=64, verbose_name='가수')),
                ('genre', models.CharField(max_length=32, verbose_name='장르')),
                ('lyrics', models.TextField(verbose_name='가사')),
                ('comment', models.TextField(verbose_name='평가')),
                ('file_path', models.CharField(max_length=512, verbose_name='파일경로')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='album.AlbumOwn', verbose_name='앨범')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.CUser', verbose_name='사용자')),
            ],
            options={
                'verbose_name': '자작곡',
                'verbose_name_plural': '자작곡',
                'db_table': 'song_own',
            },
        ),
        migrations.CreateModel(
            name='SongCovered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='노래제목')),
                ('vocal', models.CharField(max_length=64, verbose_name='가수')),
                ('vocal_origin', models.CharField(max_length=64, verbose_name='원곡 가수')),
                ('lyrics', models.TextField(verbose_name='가사')),
                ('comment', models.TextField(verbose_name='평가')),
                ('genre', models.CharField(max_length=32, verbose_name='장르')),
                ('file_path', models.CharField(max_length=512, verbose_name='파일경로')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='album.AlbumCovered', verbose_name='앨범')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.CUser', verbose_name='사용자')),
            ],
            options={
                'verbose_name': '커버곡',
                'verbose_name_plural': '커버곡',
                'db_table': 'song_covered',
            },
        ),
    ]