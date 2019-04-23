from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,CreateView,
                                    DetailView, ListView,)
from .forms import PostForm, ContactForm
from .models import Post
from django.utils import timezone
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

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


def contact_email(request):

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = request.user.email
            recipients = ['kiran.gangadhar.01@gmail.com']
            recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('thankyou.html')  # Redirect after POST
    else:
        form = ContactForm()  # An unbound form
    return render(request, 'computers/contact-us.html', {'form': form, })
