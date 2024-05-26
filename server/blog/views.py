from django.shortcuts import render , redirect
from .forms import BlogForm
from .models import Blog
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    blogs = Blog.objects.all()
    page_number  = request.GET.get('page')
    p = Paginator(blogs,3)
    try:
        page_obj = p.get_page(page_number)  
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    context = {
        'page_obj':page_obj
    }
    return render(request,'index.html',context)


def Blog_Create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            image = form.cleaned_data.get("image")
            print('the image',image)
            print('the image',image)
            print('the image',image)
            print('the image',image)
            print('the image',image)
            print('the other values',title,content)
            form.save()
            return redirect('/')
        else:
            return redirect('/')


def Views_Blog(request,id):
    instance = Blog.objects.get(id = id)
    context = {
        'blog':instance
    }
    return render(request,'views.html',context)
    