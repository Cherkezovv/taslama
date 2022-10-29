from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import Okuwcy

class OkuwcyForm(forms.ModelForm):
	class Meta:
		model = Okuwcy
		fields = ['okuwcy_ady', 'okuwcy_familya', 'okuwcy_welayat', 'okuwcy_etrap', 'okuwcy_mekdep', 'okuwcy_synp', 'okuwcy_phone']
