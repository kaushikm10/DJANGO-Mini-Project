from django.contrib import admin
from .models import Blogger, Comments, Followers, Post
# Register your models here.

admin.site.register(Blogger)
admin.site.register(Comments)
admin.site.register(Followers)
admin.site.register(Post)
