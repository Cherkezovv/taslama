from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import GyzyklyVideo, Habar, GyzyklyKitap
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def gyzykly_videolar(request):
	gyzykly_videolar = GyzyklyVideo.objects.order_by('-date_added')
	paginator = Paginator(gyzykly_videolar, 25)
	page = request.GET.get('page')
	try:
		gyzykly_video = paginator.page(page)
	except PageNotAnInteger:
		gyzykly_video = paginator.page(1)
	except EmptyPage:
		gyzykly_video = paginator.page(paginator.num_pages)
	
	context = {'gyzykly_videolar': gyzykly_video, 'page': page}
	return render(request, 'gyzykly/gyzykly_videolar.html', context)


@login_required
def gyzykly_kitaplar(request):
	gyzykly_kitaplar = GyzyklyKitap.objects.order_by('-date_added')
	paginator = Paginator(gyzykly_kitaplar, 25)
	page = request.GET.get('page')

	try:
		gyzykly_kitap = paginator.page(page)
	except PageNotAnInteger:
		gyzykly_kitap = paginator.page(1)
	except EmptyPage:
		gyzykly_kitap = paginator.page(paginator.num_pages)

	context = {'gyzykly_kitaplar': gyzykly_kitap, 'page': page}
	return render(request, 'gyzykly/gyzykly_kitaplar.html', context)


@login_required	
def habarlar(request):
	habarlar = Habar.objects.order_by('-date_added')
	paginator = Paginator(habarlar, 2)
	page = request.GET.get('page')
	try:
		habar = paginator.page(page)
	except PageNotAnInteger:
		habar = paginator.page(1)
	except EmptyPage:
		habar = paginator.page(paginator.num_pages)

	context = {'habarlar': habar, 'page': page}
	return render(request, 'gyzykly/habarlar.html', context)


@login_required
def habar(request, p_k):
	sonky_habarlar = Habar.objects.order_by('-date_added')[:6]
	habar = Habar.objects.get(id=p_k)
	context = {'habar': habar, 'sonky_habarlar': sonky_habarlar}
	return render(request, 'gyzykly/habar.html', context)