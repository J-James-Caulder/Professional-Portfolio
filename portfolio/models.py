from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=40, blank=False)
    description = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='portfolio/images/', blank=True)
    sample = models.FileField(upload_to='portfolio/uploads/', blank=True)

    def __str__(self):
        return self.title

class Future(models.Model):
    title = models.CharField(max_length=40, blank=False)
    platform = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='portfolio/images/', blank=True)
    release = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.title

class Finished(models.Model):
    title = models.CharField(max_length=40, blank=False)
    platform = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='portfolio/images/', blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Recording(models.Model):
    title = models.CharField(max_length=50, blank=False)
    Song = 'Song'
    Audiobook = 'Audiobook'
    Animation = 'Animation'
    Commercials = 'Commercials'
    Announcing = 'Announcing'
    Audio_Work_Choices =  [
        (Song, 'Song'),
        (Audiobook, 'Audiobook'),
        (Animation, 'Animation'),
        (Commercials, 'Commercials'),
        (Announcing, 'Announcing'),
    ]
    Audio_Work = models.CharField(
        max_length=20,
        choices=Audio_Work_Choices,
        default=Animation,
        )
    sample = models.FileField(upload_to='portfolio/uploads/', blank=True)

    def __str__(self):
        return self.Audio_Work
