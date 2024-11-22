from .models import Profiler
from django import forms

class ProfilerForm(forms.ModelForm):
    class Meta:
        model = Profiler
        fields = ('profile_image', 'profile_bio',)