from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    Form for handling collaboration requests.

    Creates a form based on the CollaborateRequest model with fields for
    name, email, and message.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('collaborator_name', 'collaborator_email', 'collaboration_message')
