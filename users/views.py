from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from . forms import UserRegistrationForm, UserLoginForm
from . import models
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.


class CreateUserView(CreateView):
    model = models.User
    form_class = UserRegistrationForm
    template_name = 'users/register_form.html'
    success_url = 'users/login'


class LoginUserView(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login_form.html'
    redirect_authenticated_user = False


def logout_view(request):
    logout(request)
    return redirect('rooms:resource_list')