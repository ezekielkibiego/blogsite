from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("contact/", contact, name="contact"),
    path("blogs/", blogs, name="blogs"),
    path("add_blog/", add_post, name="add_post"),
    path('bloglist/', BlogListView.as_view(), name='bloglist'),
    path('editors/', editor_list, name='editors'),


]