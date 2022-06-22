from audioop import reverse
from dataclasses import field
from sre_constants import SUCCESS
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import models
from django.urls import reverse_lazy

from I4G0228411SD.blog.admin import Post
# Create your views here.
def PostListView(request):
    model = Post

def PostCreateView(request):
    model = Post
    field = "__all__"
    success_url = reverse_lazy("blog:all")

def PostDetailsView(request):
    model = Post

def PostUpdateView(request):
    model = Post
    field = "__all__"
    success_url = reverse_lazy("blog:all")

def PostDeleteView(request):
    model = Post
    field = "__all__"
    success_url = reverse_lazy("blog:all")
