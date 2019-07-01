from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    edition = models.CharField(max_length=10)
    thumbnail = models.ImageField(upload_to='images')
    kindle = models.FileField(upload_to='files')
    slug = models.SlugField(unique=True)
    published = models.DateTimeField()
    def __str__(self):
        return  self.title
