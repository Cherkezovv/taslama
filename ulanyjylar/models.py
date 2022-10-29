from django.db import models
from django.contrib.auth.models import User

class Okuwcy(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE)
#	okuwcy_image = models.ImageField('Suraty', upload_to='okuwcylar/')
	okuwcy_ady = models.CharField('Okuwcynyn ady', max_length=200)
	okuwcy_familya = models.CharField('Okuwcynyn familyasy', max_length=200)
	okuwcy_welayat = models.CharField('Welayaty', max_length=200)
	okuwcy_etrap = models.CharField('Etraby', max_length=200)
	okuwcy_mekdep = models.PositiveIntegerField('Mekdebi', default=1)
	okuwcy_synp = models.PositiveIntegerField('Synpy', default=4)
	okuwcy_phone = models.PositiveIntegerField('Okuwcynyn telefon belgisi')

	def __str__(self):
		return self.okuwcy_ady + self.okuwcy_familya

	class Meta:
		verbose_name = 'okuwcy'
		verbose_name_plural = 'Okuwçylar'


