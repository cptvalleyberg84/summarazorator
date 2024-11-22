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
    title = forms.CharField(
        validators=[MinLengthValidator(5)],
        help_text='Title must be at least 5 characters long'
    )
    content = forms.CharField(
        widget=SummernoteWidget(),
        validators=[MinLengthValidator(20)],
        help_text='Content must be at least 20 characters long'
    )
    excerpt = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        help_text='A brief summary of your post'
    )

    def clean_featured_image(self):
        image = self.cleaned_data.get('featured_image')
        if image:
            
            if hasattr(image, 'size'):
                if image.size > 5 * 1024 * 1024:  
                    raise forms.ValidationError("Image file too large ( > 5MB )")
        return image

    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image', 'excerpt', 'status']