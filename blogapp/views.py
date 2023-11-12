from django.shortcuts import redirect, render
from rest_framework import status
from blogapp.forms import BlogForm
from blogapp.serializers import BlogSerializer
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response

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


class BlogListView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

