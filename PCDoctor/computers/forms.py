from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }


class ContactForm(forms.Form):
    subject = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subject'}) )
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder':'your message' , 'class':'form-control editable medium-editor-textarea postcontent'}),)
    sender = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'your Email', 'class':'form-control'}))
