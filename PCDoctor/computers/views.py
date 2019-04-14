from django.shortcuts import render
from django.views.generic import (TemplateView,)

# Create your views here.
class AboutView(TemplateView):
    template_name = 'computers/about-us.html'

class BlogView(TemplateView):
    template_name = 'computers/blog.html'
