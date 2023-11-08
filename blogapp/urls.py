from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("blogs/",views.blogs, name="blogs"),
    path("add_blog/", views.add_post, name="add_post")

]