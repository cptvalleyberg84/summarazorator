from .models import Comment
from django import forms
from django.core.validators import MinLengthValidator


class CommentForm(forms.ModelForm):
    body = forms.CharField(validators=[MinLengthValidator(12)])
    class Meta:
        model = Comment
        fields = ('body',)

