from .models import CollaborateRequest
from django import forms


class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('collaborator_name', 'collaborator_email', 'collaboration_message')