from django import forms
from .models import Profiler


class ProfilerForm(forms.ModelForm):
    """
    Form for editing user profile information.
    Allows users to update their profile image and bio.
    """
    class Meta:
        model = Profiler
        fields = ('profile_image', 'profile_bio')
