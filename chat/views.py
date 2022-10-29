from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Sorag, AdmineHabar
from .forms import SoragForm, AdmineHabarForm
from ulanyjylar.models import Okuwcy



@login_required
def soragjogap(request):
	okuwcydata = Okuwcy.objects.filter(username=request.user)
	okuwcyform = Okuwcy.objects.get(username=request.user)

	soraglar = Sorag.objects.order_by('date_added')

	if request.method != 'POST':
		form = SoragForm()
	else:
		form = SoragForm(data=request.POST)
		if form.is_valid():
			taze_sorag = form.save(commit=False)
			taze_sorag.owner = okuwcyform
			taze_sorag.save()
			return redirect('chat:sorag_jogap')
	context = {'soraglar': soraglar, 'okuwcydata': okuwcydata, 'form': form}
	return render(request, 'chat/soraglar.html', context)


@login_required
def adminehabar(request):

	if request.method != 'POST':
		form = AdmineHabarForm()
	else:
		form = AdmineHabarForm(request.POST, request.FILES)
		if form.is_valid():
			taze_habar = form.save(commit=False)
			taze_habar.owner = request.user
			taze_habar.save()
			return redirect('books_videos:index')
	context = {'form': form}
	return render(request, 'chat/adminehabar.html', context)