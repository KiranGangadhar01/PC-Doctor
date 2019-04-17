from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,CreateView,
                                    DetailView, ListView,)
from .forms import PostForm
from .models import Post
from django.utils import timezone

# Create your views here.
class AboutView(TemplateView):
    template_name = 'computers/about-us.html'

class BlogView(ListView):
    template_name = 'computers/blog.html'

    def get_queryset(self):
        return Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')

class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'computers/post_detail.html'

    form_class = PostForm

    model = Post

class PostDetailView(DetailView):
    model = Post
