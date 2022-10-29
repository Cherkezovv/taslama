from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ders, Book, Video 
from gyzykly.models import Surat, GyzyklyVideo, GyzyklyKitap, Habar
from ulanyjylar.models import Okuwcy
from chat.models import Sorag
from .forms import BellikForm
from django.http import Http404

@login_required
def index(request):
	suratlar = Surat.objects.order_by('-date_added')
	dersler = Ders.objects.all()
	habarlar = Habar.objects.order_by('-date_added')[:6]
	gyzykly_videolar = GyzyklyVideo.objects.order_by('-date_added')[:6]
	gyzykly_kitaplar = GyzyklyKitap.objects.order_by('-date_added')[:6]
	soraglar = Sorag.objects.order_by('-date_added')[:6]
	okuwcydata = Okuwcy.objects.filter(username=request.user)
	context = {'dersler': dersler, 'suratlar': suratlar, 'gyzykly_videolar': gyzykly_videolar, 'gyzykly_kitaplar':gyzykly_kitaplar, 'habarlar': habarlar, 'okuwcydata': okuwcydata, 'soraglar': soraglar}
	return render(request, 'books_videos/index.html', context)


@login_required
def kitaplar_videolar(request, pk):
	ders = Ders.objects.get(id=pk)
	kitaplar = ders.book_set.order_by('-date_added')
	videolar = ders.video_set.order_by('-date_added')
	bellikler = ders.bellik_set.filter(owner=request.user).order_by('-date_added')

	if request.method != 'POST':
		form = BellikForm()
	else:
		form = BellikForm(data=request.POST)
		if form.is_valid():
			taze_bellik = form.save(commit=False)
			taze_bellik.owner = request.user
			taze_bellik.ders = ders
			taze_bellik.save()
			return redirect('books_videos:kitaplar_videolar', pk)

	context = {'ders': ders, 'kitaplar': kitaplar, 'videolar': videolar, 'bellikler': bellikler, 'form': form}
	return render(request, 'books_videos/kitaplar_videolar.html', context)




