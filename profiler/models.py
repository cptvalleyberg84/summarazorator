from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from forum.models import Post, Comment

# Create your models here.

class Profiler(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profiler")
    image = CloudinaryField('image', default='placeholder')
    bio = models.TextField(blank=True, max_length=500)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    last_posts = models.ManyToManyField(Post, blank=True, related_name="profile_posts") 
    last_comments = models.ManyToManyField(Comment, blank=True, related_name="profile_comments") 
    
    def __str__(self):
        return f"{self.user.username}'s Profile"