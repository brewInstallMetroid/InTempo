from django.db import models

# Create your models here.
class Challenge(models.Model):
	song = models.CharField(max_length=255)
	artist = models.CharField(max_length=255)
	youtube_link = models.CharField(max_length=255)
	clip_1 = models.FileField(upload_to="audio/")
	clip_2 = models.FileField(upload_to="audio/")
	clip_3 = models.FileField(upload_to="audio/")
        
	def __str__(self):
		return f"{self.song} - {self.artist}"

