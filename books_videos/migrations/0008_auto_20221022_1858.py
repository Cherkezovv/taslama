# Generated by Django 3.0.4 on 2022-10-22 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_videos', '0007_auto_20221022_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.CharField(default=1, max_length=200, verbose_name='Kitabyn ady'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='name',
            field=models.CharField(default=1, max_length=200, verbose_name='Videonyn ady'),
            preserve_default=False,
        ),
    ]
