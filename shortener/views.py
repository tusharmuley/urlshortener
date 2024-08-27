from django.shortcuts import render, redirect, get_object_or_404
from .models import URL

def shorten_url(request):
    if request.method == "POST":
        original_url = request.POST['url']
        url, created = URL.objects.get_or_create(original_url=original_url)
        return render(request, 'shortener/shorten_url.html', {'url': url})
    return render(request, 'shortener/shorten_url.html')

def redirect_url(request, short_url):
    url = get_object_or_404(URL, short_url=short_url)
    return redirect(url.original_url)
