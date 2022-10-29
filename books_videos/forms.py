from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import Bellik

class BellikForm(forms.ModelForm):
	class Meta:
		model = Bellik
		fields = ['tema_name', 'tema_text']
		widgets = {
			"tema_name": TextInput(attrs={
				'class': 'block p-2 h-8 w-full my-2 text-sm text-gray-900 bg-gray-50 rounded-sm border border-gray-300 focus:ring-blue-500 focus:border-blue-500',
				'placeholder': 'Teman adyny giriz...',
				}),
			"tema_text": Textarea(attrs={
				'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500',
				'placeholder': 'Sizin belligniz...',
				'rows': 4
				}),
		}