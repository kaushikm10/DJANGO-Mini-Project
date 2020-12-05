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


class Comments(models.Model):
    comment_by = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(default=datetime.datetime.now())
    


class Followers(models.Model):
    follower = models.ForeignKey(Blogger, on_delete=models.CASCADE, related_name='follower', default=None)
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE, related_name='blogger', default=None)
