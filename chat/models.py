from django.db import models
from ulanyjylar.models import Okuwcy
from django.contrib.auth.models import User


class Sorag(models.Model):
	owner = models.ForeignKey(Okuwcy, on_delete=models.CASCADE)
	sorag = models.TextField('Sorag')
	date_added = models.DateTimeField('gosulan wagty', auto_now_add=True)

	def __str__(self):
		return self.owner.okuwcy_ady + ' ' + self.owner.okuwcy_familya + ' soragy: ' + self.sorag + ' gosulan wagty ' + str(self.date_added)

	class Meta:
		verbose_name = 'sorag'
		verbose_name_plural = 'SoragJogaplar'



class AdmineHabar(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()
	file = models.FileField(upload_to='adminefile/')
	date_added = models.DateTimeField('gosulan wagty', auto_now_add=True)

	def __str__(self):
		return self.owner.username + self.text + str(self.date_added)

	class Meta:
		verbose_name = 'ulanyjydan habar'
		verbose_name_plural = 'Ulanyjydan admine habar'