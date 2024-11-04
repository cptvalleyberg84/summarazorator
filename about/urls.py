from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_srzr, name='about'),
]