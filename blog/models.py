from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(verbose_name="标签",max_length=10)

    def __str__(self):
        return self.type_name

class Blog(models.Model):
    blog_title = models.CharField(verbose_name="标题",max_length=30)
    blog_content = models.TextField(verbose_name="内容")
    blog_type = models.ForeignKey(BlogType,verbose_name="分类",on_delete=models.DO_NOTHING)
    blog_author = models.ForeignKey(User,verbose_name="作者",on_delete=models.DO_NOTHING)
    blog_create_time = models.DateTimeField(verbose_name="创建时间",auto_now_add=True)
    blog_modify_time = models.DateTimeField(verbose_name="更新时间",auto_now=True)
    blog_images = models.ImageField(verbose_name="配图",upload_to='uploads/%Y/%m/%d/')

    def __str__(self):
        return self.blog_title

    class Meta:
        ordering = ['-blog_create_time']