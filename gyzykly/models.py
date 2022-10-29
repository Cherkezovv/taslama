from django.db import models


class Surat(models.Model):
	image_name = models.CharField('Suratyn ady', max_length=200)
	image = models.ImageField('Surat', upload_to='images/')
	date_added = models.DateTimeField('gosulan wagty', auto_now_add=True)

	def __str__(self):
		return self.image_name
		
	class Meta:
		verbose_name = 'surat'
		verbose_name_plural = 'Suratlar'


class GyzyklyVideo(models.Model):
	gyzykly_video_name = models.CharField('Videonyn ady', max_length=200)
	gyzykly_video = models.FileField('Video', upload_to='gyzykly_video/')
	date_added = models.DateTimeField('gosulan wagty', auto_now_add=True)

	def __str__(self):
		return self.gyzykly_video_name

	class Meta:
		verbose_name = 'video'
		verbose_name_plural = 'Videolar'


class Habar(models.Model):
	habar_image = models.ImageField('Habaryn suraty', upload_to='habarlar/')
	habar_name = models.CharField('Habaryn ady', max_length=250)
	habar_text = models.TextField()
	date_added = models.DateTimeField('gosulan wagty', auto_now_add=True)


	def __str__(self):
		return self.habar_name 

	class Meta:
		verbose_name = 'habar'
		verbose_name_plural = 'Habarlar'


class GyzyklyKitap(models.Model):
	gyzykly_kitap_name = models.CharField('Kitapyn ady', max_length=200)
	gyzykly_kitap = models.FileField('Kitap', upload_to='gyzykly_kitap/')
	date_added = models.DateTimeField('gosulan wagty', auto_now_add=True)

	def __str__(self):
		return self.gyzykly_kitap_name

	class Meta:
		verbose_name = 'kitap'
		verbose_name_plural = 'Kitaplar'
