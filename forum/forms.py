from .models import Comment, Post
from django import forms
from django.core.validators import MinLengthValidator
from django_summernote.widgets import SummernoteWidget



class CommentForm(forms.ModelForm):
    body = forms.CharField(validators=[MinLengthValidator(12)])
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image', 'excerpt', 'status']
        widgets = {
            'content': SummernoteWidget(),
        }