from django import forms
from django.contrib.auth.models import User
from .models import Blog
class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        exclude=['slug','user']
        widgets={
            'body':forms.Textarea(attrs={'cols':80,'rows':30})
        }