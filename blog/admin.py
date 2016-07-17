from django.contrib import admin

# Register your models here.
# Esto lo puse yo
from .models import Post

admin.site.register(Post)