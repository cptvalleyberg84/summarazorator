from django.urls import path
from . import views


urlpatterns = [
    path('', views.profiler_page, name='profiler'),
    path('edit/<int:profiler_id>/', views.profiler_edit, name='profiler_edit'),
    path('profiler/<int:pk>/delete/', views.profile_delete, name='profiler_delete'),
    path('user/<str:username>/', views.view_profile, name='view_profile'),
]
