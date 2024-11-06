from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.profiler_page, name='profiler'),
]