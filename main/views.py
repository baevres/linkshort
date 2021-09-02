from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from django.utils import timezone

from .models import *
from .base import *

import datetime


def create_url(in_model, lst):
    """
    Creating records in model ShortLink with using functions search() and generator() from base.py.
    At first main_page will use search() for checking input string and then gives lst here.
    Infinity circle <while> will generate new string and try save it in model while it is possible and don`t call the IntegrityError.
    If record exists, circle will be continue.
    """
    in_model.end_time = datetime.datetime.now(tz=None) + datetime.timedelta(hours=1)
    while True:
        try:
            dec = generator()
            in_model.short_url = lst + next(dec)[0]
            in_model.save()
            break
        except IntegrityError:
            continue
    return


def main_page(request):
    if request.method == 'POST':
        url = request.POST['url']
        lst = search(url)
        if lst:
            in_model = ShortLink.objects.get_or_create(url=url)[0]
            if not in_model.short_url:
                create_url(in_model, lst[0])

                return redirect('url_page', in_model.id)
            else:
                return redirect('url_page', in_model.id)

    last_urls = ShortLink.objects.all().order_by('-end_time')
    if len(last_urls) >= 6:
        last_urls = last_urls[:6]
    context = {
        'title': 'LinkShort - сократит ссылку в миг',
        'urls': last_urls
    }
    return render(request, 'main/main_page.html', context)


def url_page(request, url_id):
    now = timezone.make_aware(datetime.datetime.now(), timezone.get_default_timezone())

    current_url = ShortLink.objects.get(pk=url_id)

    if now >= current_url.end_time:
        lst = search(current_url.url)
        create_url(current_url, lst[0])
        return redirect('url_page', url_id)

    context = {
        'title': 'Сокращенная ссылка',
        'current_url': current_url,

    }
    return render(request, 'main/url_page.html', context)


def about_page(request):
    context = {
        'title': 'О нас',
    }
    return render(request, 'main/about_page.html', context)
