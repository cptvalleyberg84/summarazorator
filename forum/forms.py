from .models import Comment, Post
from django import forms
from django.core.validators import MinLengthValidator
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    comment_body = forms.CharField(validators=[MinLengthValidator(12)])
    class Meta:
        model = Comment
        fields = ('comment_body',)

class PostForm(forms.ModelForm):
    post_title = forms.CharField(
        validators=[MinLengthValidator(5)],
        help_text='Title must be at least 5 characters long'
    )
    post_content = forms.CharField(
        widget=SummernoteWidget(),
        validators=[MinLengthValidator(20)],
        help_text='Content must be at least 20 characters long'
    )
    post_excerpt = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        help_text='A brief summary of your post'
    )

    def clean_post_featured_image(self):
        image = self.cleaned_data.get('post_featured_image')
        if image:

            if hasattr(image, 'size'):
                if image.size > 5 * 1024 * 1024: 
                    raise forms.ValidationError("Image file too large ( > 5MB )")
        return image

    class Meta:
        model = Post
        fields = ['post_title', 'post_content', 'post_featured_image', 'post_excerpt', 'post_status']