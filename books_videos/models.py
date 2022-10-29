from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


class Ders(models.Model):
	ders_name = models.CharField('Dersin ady', max_length=200)
	ders_synp = models.PositiveIntegerField('Dersin synpy', default=4)

	def __str__(self):
		return self.ders_name + ' ' +str(self.ders_synp) + '-nji synp'

	class Meta:
		verbose_name = 'Ders'
		verbose_name_plural = 'Dersler'


class Book(models.Model):
	ders = models.ForeignKey(Ders, on_delete=models.CASCADE)
	name = models.CharField('Kitabyn ady', max_length=200)
	file = models.FileField('Kitap', upload_to='books/')
	date_added = models.DateTimeField('gosulan wagty', auto_now_add=True)

	def __str__(self):
		return self.ders.ders_name + ' ' + str(self.ders.ders_synp) + '-nji synp' + self.name  

	class Meta:
		verbose_name = 'kitap'
		verbose_name_plural = 'Kitaplar'


class Video(models.Model):
	ders = models.ForeignKey(Ders, on_delete=models.CASCADE)
	name = models.CharField('Videonyn ady', max_length=200)
	file = models.FileField('Video', upload_to='videos/')
	date_added = models.DateTimeField('gosulan wagty', auto_now_add=True)

	def __str__(self):
		return self.ders.ders_name + ' ' + str(self.ders.ders_synp) + '-nji synp' + self.name   

	class Meta:
		verbose_name = 'video'
		verbose_name_plural = 'videolar'


class Bellik(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	ders = models.ForeignKey(Ders, on_delete=models.CASCADE)
	tema_name = models.CharField('Temanyn ady', max_length=200)
	tema_text = RichTextUploadingField()
	date_added = models.DateTimeField('gosulan wagty', auto_now_add=True)

	def __str__(self):
		return self.tema_name

	class Meta:
		verbose_name = 'bellik'
		verbose_name_plural = 'Bellikler'









