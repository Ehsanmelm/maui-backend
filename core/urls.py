from . import views
from django.urls import path


urlpatterns = [
    path('register' , views.RegisterUserView.as_view()),
    path('login' , views.LoginUserView.as_view())
]