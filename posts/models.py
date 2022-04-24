
from datetime import date, datetime
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify  
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_details", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)