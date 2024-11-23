from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Profiler


@admin.register(Profiler)
class ProfilerAdmin(SummernoteModelAdmin):
    """Admin configuration for the Profiler model."""
    list_display = ('profile_user', 'profile_created_on', 'profile_updated_on')
    search_fields = ('profile_user__username', 'profile_bio')
    list_filter = ('profile_created_on', 'profile_updated_on')
    summernote_fields = ('profile_bio',)
