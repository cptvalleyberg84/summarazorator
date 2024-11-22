from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    post_title = models.CharField(max_length=200, unique=True)
    post_slug = models.SlugField(max_length=200, unique=True)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_posts")
    post_featured_image = CloudinaryField('image', default='placeholder')
    post_content = models.TextField()
    post_created_on = models.DateTimeField(auto_now_add=True)
    post_updated_at = models.DateTimeField(auto_now=True)
    post_status = models.IntegerField(choices=STATUS, default=0)
    post_excerpt = models.TextField(blank=True)

    class Meta:
        ordering = ['post_created_on']

    def __str__(self):
        return f"Post: {self.post_content} by {self.post_author}"


class Comment(models.Model):
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    comment_body = models.TextField()
    comment_created_on = models.DateTimeField(auto_now_add=True)
    comment_updated_at = models.DateTimeField(auto_now=True)
    comment_approved = models.BooleanField(default=True)

    TYPE_CHOICES = [
        ('positive', 'Positive'),
        ('negative', 'Negative'),
    ]
    comment_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='positive')

    comment_reactors = models.ManyToManyField(
        User,
        related_name='post_reactions',
        blank=True
    )

    class Meta:
        ordering = ["comment_created_on"]

    def __str__(self):
        return f"Comment: {self.comment_body} by {self.comment_author}"