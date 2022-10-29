# Generated by Django 3.0.4 on 2022-10-26 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gyzykly', '0006_auto_20221022_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='GyzyklyKitap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gyzykly_kitap_name', models.CharField(max_length=200, verbose_name='Kitapyn ady')),
                ('gyzykly_kitap', models.FileField(upload_to='gyzykly_kitap/', verbose_name='Kitap')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='gosulan wagty')),
            ],
            options={
                'verbose_name': 'kitap',
                'verbose_name_plural': 'Kitaplar',
            },
        ),
    ]
