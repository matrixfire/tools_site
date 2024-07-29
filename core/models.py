from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    cover_image = models.ImageField(upload_to='cover_images/', blank=True, null=True)
    key_points = models.JSONField(blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        return self.title
