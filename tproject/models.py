from django.db import models
from django.conf import settings


class Image(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    thumbnail_200 = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    thumbnail_400 = models.ImageField(upload_to='thumbnails/', null=True, blank=True)
    original_url = models.URLField(null=True, blank=True)
    expiration_time = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.owner}'s image ({self.image.name})"
class Level(models.Model):
    name = models.CharField(max_length=50)
    thumbnail_sizes = models.CharField(max_length=100, blank=True, default='200,400')
    original_url = models.BooleanField(default=False)
    expiring_link = models.BooleanField(default=False)
    expiration_time_min = models.PositiveIntegerField(default=300)
    expiration_time_max = models.PositiveIntegerField(default=30000)

    def __str__(self):
        return self.name
