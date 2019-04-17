from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'basic_app'

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about-us'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('post/new',views.CreatePostView.as_view(),name='post_new'),
    path('post/<int:pk>',views.PostDetailView.as_view(), name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
