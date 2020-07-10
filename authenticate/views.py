from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from .forms import SignUpForm
# Create your views here.
def home(request):
    return render(request,'index.html')
class UserLogin(LoginView):
    template_name="authenticate/login.html"
    """def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return redirect('/login')"""
    def post(self, request):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
def signup(request):
    context={}
    if request.method=='POST':
        form=SignUpForm(request.POST)
        print(form['password1'])
        """temp=User.objects.get(user=request.POST['username'])
        if temp:
            Profile.objects.create(user=request.POST)"""
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.profile.birth_date=form.cleaned_data.get('birth_date')
            print(user.profile.birth_date)
            user.save()
            user=authenticate(request,username=request.POST['username'],password=request.POST['password1'])
            login(request,user)
            return redirect('/')
        else:
            #print(form.errors.as_json())
            context['errors']=form.errors
            #print(context['errors'][0])
            context['form']=SignUpForm()
            return render(request,'authenticate/signup.html',context)
    form=SignUpForm()
    context['form']=form
    """if request.user.is_authenticated:
        return redirect('/main')"""
    return render(request, 'authenticate/signup.html',context)