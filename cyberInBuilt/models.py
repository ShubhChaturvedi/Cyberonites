from pickle import TRUE
from django.db import models
from django.utils.timezone import now
from ckeditor.fields import RichTextField

# Create your models here.
class Staff(models.Model):
    staff_sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=30)
    profile = models.ImageField()
    description = models.TextField(max_length= 250)
    linkedin = models.URLField(max_length=200)
    github = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    sno = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=260)
    content = RichTextField(blank=True,null=True)
    author = models.CharField(max_length=13)
    timestamp = models.DateTimeField(blank=True , default=now)
    slug = models.CharField(max_length=120)
    image = models.ImageField(default="default")

    def __str__(self):
        return self.title + " by " + self.author