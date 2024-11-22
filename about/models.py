from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):

    about_title = models.CharField(max_length=200)
    about_logo_image = CloudinaryField('image', default='placeholder')
    about_updated_on = models.DateTimeField(auto_now=True)
    about_content = models.TextField()

    def __str__(self):
        return self.about_title


class CollaborateRequest(models.Model):
    collaborator_name = models.CharField(max_length=200)
    collaborator_email = models.EmailField()
    collaboration_message = models.TextField()
    request_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.collaborator_name}"