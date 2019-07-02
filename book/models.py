from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self',related_name='children',on_delete=models.CASCADE,default=None,null=True,blank=True)
    def __str__(self):
        return self.name
    def has_children(self):
        return self.children.exists()
    def has_parent(self):
        return True if self.parent else False

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    edition = models.CharField(max_length=10)
    thumbnail = models.ImageField(upload_to='images')
    kindle = models.FileField(upload_to='files')
    slug = models.SlugField(unique=True)
    published = models.DateTimeField()
    category = models.ForeignKey(Category,related_name='books',on_delete=models.CASCADE)
    def __str__(self):
        return  self.title
