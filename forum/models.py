from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS_CHOICES = (
    (0, "Draft"),
    (1, "Published")
)

COMMENT_TYPE_CHOICES = [
    ('positive', 'Positive'),
    ('negative', 'Negative'),
]


class Post(models.Model):
    """
    Model representing a forum post.
    Stores information about posts including title, content,
    author, and publication status.
    """
    post_title = models.CharField(
        max_length=200,
        unique=True,
        help_text="Title of the post"
    )
    post_slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text="URL-friendly version of the title"
    )
    post_author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="forum_posts"
    )
    post_featured_image = CloudinaryField(
        'image',
        default='placeholder'
    )
    post_content = models.TextField(
        help_text="Main content of the post"
    )
    post_excerpt = models.TextField(
        blank=True,
        help_text="Brief summary of the post"
    )
    post_created_on = models.DateTimeField(auto_now_add=True)
    post_updated_at = models.DateTimeField(auto_now=True)
    post_status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=0,
        help_text="0: Draft, 1: Published"
    )

    class Meta:
        ordering = ['-post_created_on']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        """Return a string representation of the post."""
        return self.post_title


class Comment(models.Model):
    """
    Model representing a comment on a forum post.
    Stores information about comments including the parent post,
    author, content, and reaction type.
    """
    parent_post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"
    )
    comment_author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="commenter"
    )
    comment_body = models.TextField(
        help_text="Content of the comment"
    )
    comment_type = models.CharField(
        max_length=10,
        choices=COMMENT_TYPE_CHOICES,
        default='positive',
        help_text="Whether the comment is positive or negative"
    )
    comment_created_on = models.DateTimeField(auto_now_add=True)
    comment_updated_at = models.DateTimeField(auto_now=True)
    comment_approved = models.BooleanField(
        default=True,
        help_text="Whether the comment is approved for display"
    )
    comment_reactors = models.ManyToManyField(
        User,
        related_name='post_reactions',
        blank=True,
        help_text="Users who have reacted to this comment"
    )

    class Meta:
        ordering = ['-comment_created_on']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        """Return a string representation of the comment."""
        return f"Comment by {self.comment_author} on {self.parent_post.post_title}"
