from django.contrib import admin
from .models import Post

# To show the posts in our admin site
admin.site.register(Post)
