from django.db import models


class ShortLink(models.Model):
    url = models.TextField('Полученная ссылка', unique=True)
    short_url = models.CharField('Короткая ссылка', max_length=100, null=True, unique=True)
    end_time = models.DateTimeField('Дедлайн ссылки', null=True)
