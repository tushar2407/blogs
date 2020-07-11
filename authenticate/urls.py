from django.urls import path
from . import views
app_name='authenticate'
urlpatterns=[
    path('',views.home, name='home'),
    path('login/',views.UserLogin.as_view(),name='login'),
    path('signup/',views.signup,name="signup")
]