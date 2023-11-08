from django.shortcuts import redirect, render

from blogapp.forms import BlogForm
from .models import *

def index(request):
 
    return render(request, "index.html")

def contact(request):
 
    return render(request, "contact.html")

def blogs(request):
    blogs = Blog.objects.all()
    ctx  = {"blogs": blogs}

    return render(request, "blogs.html", ctx)


def add_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            blog = form.save(commit=False)
            
            blog.save()

            form = BlogForm()

            return redirect("/blogs")
        
    else:
        form = BlogForm()


    return render(request, "blogForm.html", {"form": form})
