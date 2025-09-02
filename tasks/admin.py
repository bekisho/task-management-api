from django.contrib import admin

# Register your models here.

# tasks/admin.py
from django.contrib import admin
from .models import User, Task, Category, Comment

admin.site.register(User)
admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Comment)


