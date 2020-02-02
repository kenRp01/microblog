from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from.models import Blog
from.forms import BlogForm

class BlogListView(ListView):
    model = Blog
    paginate_by = 5
    context_object_name="blogs"

class BlogDetailView(DetailView):
    model = Blog
    context_object_name="blog"

class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("index")
    template_name="blog/blog_create_form.html"

class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "blog/blog_update_form.html"

    def get_success_url(self):
        blog_pk = self.kwargs['pk']
        url = reverse_lazy("detail", kwargs={"pk": blog_pk})
        return url

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("index")