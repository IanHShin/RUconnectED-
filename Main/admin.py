from django.contrib import admin
from .models import Profile, Text_Post
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.

admin.site.register(Profile)
admin.site.register(Text_Post)