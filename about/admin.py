from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, CollaborateRequest


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """Admin configuration for the About model."""
    summernote_fields = ('about_content',)


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """Admin configuration for the CollaborateRequest model."""
    list_display = ('collaborator_name', 'collaborator_email', 'collaboration_message', 'request_read',)
