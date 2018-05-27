from django.contrib import admin
from .models import BlogType,Blog
# Register your models here.
@admin.register(BlogType)
class BlogType(admin.ModelAdmin):
    list_display = ['type_name']

@admin.register(Blog)
class Blog(admin.ModelAdmin):
    list_display = ('blog_title','blog_content','blog_type','blog_author','blog_create_time','blog_modify_time')