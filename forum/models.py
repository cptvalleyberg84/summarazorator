from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Post: {self.content} by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    TYPE_CHOICES = [
        ('positive', 'Positive'),
        ('negative', 'Negative'),
    ]
    comment_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='positive')

    reactors = models.ManyToManyField(
        User,
        related_name='post_reactions',
        blank=True
    )

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment: {self.body} by {self.author}"