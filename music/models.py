from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=150)
    year = models.CharField(max_length=4)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.title} - {self.artist}"

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file_type = models.CharField(max_length=4)
    is_favorite = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} from the album {self.album}"