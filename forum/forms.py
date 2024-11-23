from django import forms
from django.core.validators import MinLengthValidator
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """Form for creating and editing comments."""
    comment_body = forms.CharField(
        validators=[MinLengthValidator(12)],
        widget=forms.Textarea(attrs={'rows': 4}),
        help_text='Comment must be at least 12 characters long'
    )

    class Meta:
        model = Comment
        fields = ('comment_body',)


class PostForm(forms.ModelForm):
    """Form for creating and editing forum posts."""
    post_title = forms.CharField(
        validators=[MinLengthValidator(5)],
        help_text='Title must be at least 5 characters long',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    post_content = forms.CharField(
        widget=SummernoteWidget(),
        validators=[MinLengthValidator(20)],
        help_text='Content must be at least 20 characters long'
    )
    post_excerpt = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        help_text='A brief summary of your post'
    )

    def clean_post_featured_image(self):
        """Validate that the uploaded image is not too large."""
        image = self.cleaned_data.get('post_featured_image')
        if image and hasattr(image, 'size'):
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError(
                    "Image file too large (maximum size is 5MB)"
                )
        return image

    class Meta:
        model = Post
        fields = [
            'post_title',
            'post_content',
            'post_featured_image',
            'post_excerpt',
            'post_status'
        ]
