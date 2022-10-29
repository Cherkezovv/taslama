from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Okuwcy
from .forms import OkuwcyForm


def logoutt(request):
	logout(request)
	return redirect('books_videos:index')


def register(request):
	if request.method != 'POST':
		form = UserCreationForm()
		form2 = OkuwcyForm()
	else:
		form = UserCreationForm(data=request.POST)
		form2 = OkuwcyForm(data=request.POST)

		if form.is_valid() and form2.is_valid():
			new_user = form.save()
			authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
			login(request, authenticated_user)
			new_okuwcy = form2.save(commit=False)
			new_okuwcy.username = request.user
			new_okuwcy.save()
			return redirect('books_videos:index')

	context = {'form': form, 'form2': form2}
	return render(request, 'registration/register.html', context)



@login_required
def shahsy_otag(request):
	okuwcydata = Okuwcy.objects.filter(username=request.user)
	context = {'okuwcydata': okuwcydata}
	return render(request, 'registration/shahsy_otag.html', context)

