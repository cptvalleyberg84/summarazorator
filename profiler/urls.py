from . import views
from django.urls import path

urlpatterns = [
    path('', views.profiler_page, name='profiler'),
    path('edit/<int:profiler_id>/', views.profiler_edit, name='profiler_edit'),
]