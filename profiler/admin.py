from django.contrib import admin
from .models import Profiler
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Profiler)
class ProfilerAdmin(SummernoteModelAdmin):

    summernote_fields = ('bio',)