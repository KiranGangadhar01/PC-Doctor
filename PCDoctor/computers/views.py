from django.shortcuts import render
from django.views.generic import (TemplateView,)

# Create your views here.
class BasicView(TemplateView):
    template_name = 'computers/about-us.html'
