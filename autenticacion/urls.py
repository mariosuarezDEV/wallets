from django.urls import path, re_path, include
from allauth.account.views import SignupView
from .views import MyCustomSignupView

urlpatterns = [
    path('registrarse/', MyCustomSignupView.as_view(), name='account_signup'),
]