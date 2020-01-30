from django.shortcuts import render
import django.views.generic import ListView

from.models import Blog

class BlogListView(ListView):
    model = Blog
