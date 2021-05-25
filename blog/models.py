from django.db import models
from ckeditor.fields import RichTextField
class Blog(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    preview = models.TextField()
    blog =RichTextField()
    views = models.IntegerField(default=2000,blank=True,null=True)
    comments = models.IntegerField(default=20,blank=True,null=True)
    author=models.CharField(max_length=50)
    reading_time=models.IntegerField(blank=True,null=True)
    date=models.DateField( auto_now=True)
    image_link=models.CharField(max_length=2000, null=False,blank=False)
    def __str__(self):
        return self.title
    
