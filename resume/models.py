from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Resume(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Age = models.CharField(max_length=30)
    Nationality = models.CharField(max_length=30)
    Freelancer = models.CharField(max_length=30, default="Available")
    Contry = models.CharField(max_length=30)
    Address = models.CharField(max_length=30)
    Phone = models.CharField(max_length=20)
    Email = models.CharField(max_length=30)
    Skype = models.CharField(max_length=30)
    Languages = models.CharField(max_length=30)


class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=120)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
	

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('resume:detail', kwargs={'slug': self.slug})    
   


