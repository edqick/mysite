from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import BlogType,Blog
# Create your views here.

def blogs(request):
    context = {}
    all_blogs = Blog.objects.all()
    all_types = BlogType.objects.all()
    hot_blogs =all_blogs[:9]
    type_blogs = all_types[:9]
    context['blogs'] = all_blogs
    context['hot_blogs'] = hot_blogs
    context['type_blogs'] = type_blogs
    return render(request,"blogs.html",context)

def types(request,id=None):
    context = {}
    all_blogs = Blog.objects.all()
    all_types = BlogType.objects.all()
    hot_blogs = all_blogs[:9]
    type_blogs = all_types[:9]
    context['blogs'] = all_blogs
    context['hot_blogs'] = hot_blogs
    context['type_blogs'] = type_blogs
    context['all_types'] = all_types
    if id is None:
        return render(request, "types_list.html", context)
    assgin_types = get_object_or_404(BlogType,id=id)
    print(assgin_types)
    assgin_type_blogs = all_blogs.filter(blog_type = assgin_types)
    print(assgin_type_blogs)
    context['assgin_types'] = assgin_types
    context['assgin_type_blogs'] = assgin_type_blogs
    return render(request, "type_blogs_list.html", context)

def blogDetails(request,id):
    context = {}
    blog_obj = get_object_or_404(Blog,id=id)
    all_blogs = Blog.objects.all()
    all_types = BlogType.objects.all()
    hot_blogs = all_blogs[:9]
    type_blogs = all_types[:9]
    context['blog'] = blog_obj
    context['blogs'] = all_blogs
    context['hot_blogs'] = hot_blogs
    context['type_blogs'] = type_blogs
    return render(request,"blog_content.html",context)
