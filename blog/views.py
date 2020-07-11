from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog
from django.http import HttpResponseRedirect
from .forms import BlogForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.
class CreateBlog(LoginRequiredMixin,CreateView):
    form_class=BlogForm
    success_url=reverse_lazy('authenticate:home')
    login_url='authenticate:login'
    template_name='blog/create.html'
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def get(self,request):
        form=BlogForm()
        print(form['body'])
        return render(request,'blog/create.html',{'form':form})