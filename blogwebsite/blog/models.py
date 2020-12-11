from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
import datetime

class Blogger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile_pics", default='profile_pics/default.png')
    about = models.TextField(blank=True)    



class Post(models.Model):
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    title = models.TextField(max_length=400)
    post = RichTextField(blank=True, null=True)
    posted_on = models.DateTimeField(default=datetime.datetime.now())
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('full_post', args=(str(self.id)))
