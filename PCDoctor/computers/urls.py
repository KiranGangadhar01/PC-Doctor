from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about-us'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('post/new',views.CreatePostView.as_view(),name='post_new'),
    path('post/<int:pk>',views.PostDetailView.as_view(), name='post_detail'),
]
