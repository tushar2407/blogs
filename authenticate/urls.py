from django.urls import path
from . import views
app_name='authenticate'
urlpatterns=[
    path('',views.home),
    path('login/',views.UserLogin.as_view()),
    path('signup/',views.signup)
]