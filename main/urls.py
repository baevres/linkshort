from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('<int:url_id>/', url_page, name='url_page'),
    path('about/', about_page, name='about_page')
]
