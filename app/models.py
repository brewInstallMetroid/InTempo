from django.db import models

class Challenge(models.Model):
    """Represents a single day's challege"""
    song = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    youtube_link = models.URLField(max_length=500)

    clip_1 = models.FileField(upload_to="audio/")
    clip_2 = models.FileField(upload_to="audio/")
    clip_3 = models.FileField(upload_to="audio/")

    def __str__(self):
        return f"{self.song} - {self.artist}"

    class Meta:
        ordering = ["song"]

