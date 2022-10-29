from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Ders, Book, Video, Bellik


class BellikAdminForm(forms.ModelForm):
	tema_text = forms.CharField(widget=CKEditorUploadingWidget())
	class Meta:
		model = Bellik
		fields = '__all__'

admin.site.register(Ders)
admin.site.register(Book)
admin.site.register(Video)


@admin.register(Bellik)
class BellikAdmin(admin.ModelAdmin):
	list_display = ['ders', 'tema_name', 'date_added']
	form = BellikAdminForm
