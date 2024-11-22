from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from forum.models import Post, Comment


class Profiler(models.Model):
    profile_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profiler")
    profile_image = CloudinaryField('image', default='placeholder')
    profile_bio = models.TextField(blank=True, max_length=500)

    profile_created_on = models.DateTimeField(auto_now_add=True)
    profile_updated_on = models.DateTimeField(auto_now=True)

    profile_last_posts = models.ManyToManyField(Post, blank=True, related_name="profile_posts") 
    profile_last_comments = models.ManyToManyField(Comment, blank=True, related_name="profile_comments") 
    
    def __str__(self):
        return f"{self.profile_user.username}'s Profile"