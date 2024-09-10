from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from .models import BlogPost


class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog/blogpost_list.html"
    context_object_name = "posts"


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/blogpost_detail.html"
    context_object_name = "post"

    def get_object(self):
        post = super().get_object()
        post.views += 1
        post.save()
        return post


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ["title", "content", "image"]
    template_name = "blog/blogpost_form.html"
    success_url = reverse_lazy("blog:blogpost_list")


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ["title", "content", "image"]
    template_name = "blog/blogpost_form.html"
    success_url = reverse_lazy("blog:blogpost_list")


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog/blogpost_confirm_delete.html"
    success_url = reverse_lazy("blog:blogpost_list")
