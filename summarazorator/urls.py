"""
URL configuration for summarazorator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404
import os

urlpatterns = [
    path('about/', include("about.urls"), name="about-urls"),
    path('accounts/', include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('profiler/', include("profiler.urls"), name="profiler-urls"),    
    path('summernote/', include('django_summernote.urls')),
    path('', include('forum.urls'), name='forum-urls'),
]

if 'DEVELOPMENT' in os.environ:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'forum.views.handler404'
