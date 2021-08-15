from django.shortcuts import render, redirect
from django.db.utils import IntegrityError

from .models import *
from .base import *
from django.utils import timezone
import datetime


def create_url(in_model):
    """
    Creating records in model ShortLink with using functions search() and decoder() from base.py.
    If record exists, the first digits after letter will be increased on 1.
    """
    in_model.end_time = (datetime.datetime.now() + datetime.timedelta(hours=1)).time()
    lst = search(in_model.url)
    dec = decoder(lst[1])

    try:
        in_model.short_url = lst[0] + dec[0]
        in_model.save()
    except IntegrityError:
        dec[1] = str(int(dec[1]) + 1)
        in_model.short_url = lst[0] + dec[0][:6]
        in_model.save()
    return


def main_page(request):
    if request.method == 'POST':
        url = request.POST['url']
        in_model = ShortLink.objects.get_or_create(url=url)[0]
        if not in_model.short_url:
            create_url(in_model)

            return redirect('url_page', in_model.id)
        else:
            return redirect('url_page', in_model.id)

    context = {
        'title': 'LinkShort - сократит ссылку в миг',

    }
    return render(request, 'main/main_page.html', context)


def url_page(request, url_id):
    now = timezone.now().time()
    current_url = ShortLink.objects.get(pk=url_id)

    if now >= current_url.end_time:
        current_url.short_url, current_url.end_time = None, None
        current_url.save()
        create_url(current_url)
        return redirect('url_page', url_id)

    context = {
        'title': 'Сокращенная ссылка',
        'current_url': current_url,
        'now': now
    }
    return render(request, 'main/url_page.html', context)


def about_page(request):
    context = {
        'title': 'О нас',
    }
    return render(request, 'main/about_page.html', context)
