from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.BasicView.as_view(), name='about-us'),
]
