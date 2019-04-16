from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,CreateView,
                                    DetailView)
from .forms import PostForm
from .models import Post

# Create your views here.
class AboutView(TemplateView):
    template_name = 'computers/about-us.html'

class BlogView(TemplateView):
    template_name = 'computers/blog.html'

class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'computers/post_detail.html'

    form_class = PostForm

    model = Post

class PostDetailView(DetailView):
    model = Post
