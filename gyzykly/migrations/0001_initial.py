# Generated by Django 3.0.4 on 2022-10-22 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GyzyklyVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gyzykly_video_name', models.CharField(max_length=200, verbose_name='Videonyn ady')),
                ('gyzykly_video', models.FileField(upload_to='gyzykly_video', verbose_name='Video')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='gosulan wagty')),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'Videolar',
            },
        ),
        migrations.CreateModel(
            name='Surat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=200, verbose_name='Suratyn ady')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Surat')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='gosulan wagty')),
            ],
            options={
                'verbose_name': 'surat',
                'verbose_name_plural': 'Suratlar',
            },
        ),
    ]
