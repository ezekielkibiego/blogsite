from django.db import models
from cloudinary.models import CloudinaryField

class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    text = models.TextField(max_length=2000)
    photo = CloudinaryField("photo", null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    

    def __str__(self):
        return self.title