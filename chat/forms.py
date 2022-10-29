from django import forms
from django.forms import ModelForm, Textarea
from .models import Sorag, AdmineHabar

class SoragForm(forms.ModelForm):
	class Meta:
		model = Sorag
		fields = ['sorag']
		widgets = {
			"sorag": Textarea(attrs={
				'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500',
				'placeholder': 'Sizin belligniz...',
				'rows': 4
				}),
		}


class AdmineHabarForm(forms.ModelForm):
	class Meta:
		model = AdmineHabar
		fields = ['text', 'file']
		widgets = {
			"text": Textarea(attrs={
				'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm',
				'placeholder': 'Sizin habarynyz...',
				'rows': 3
				}),
		}
