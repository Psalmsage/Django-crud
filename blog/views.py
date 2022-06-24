from msilib.schema import Class
from django.forms import fields_for_model
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from audioop import reverse
from dataclasses import field
from sre_constants import SUCCESS
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import models
from django.urls import reverse_lazy
from .models import Post


# Create your views here.

class PostListView(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"

class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    template_name = "blog/post_form.html"

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detailhtml"

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    template_name = "blog/post_form.html"

class PostDeleteView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
    template_name = "blog/post_confirm_html"
