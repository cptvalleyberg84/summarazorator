from django.urls import path
from . import views


urlpatterns = [
    path('', views.about_srzr, name='about'),
]
