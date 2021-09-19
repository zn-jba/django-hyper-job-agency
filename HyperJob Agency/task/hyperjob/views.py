from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from .forms import SignupForm


class IndexView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, "layout/base.html", context={"title": "Home"})


class LoginView(View):
    @staticmethod
    def get(request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = AuthenticationForm()
        context = {
            "title": "Login",
            "login_form": form,
        }
        return render(request, "auth/login.html", context)

    @staticmethod
    def post(request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username", None)
            password = form.cleaned_data.get("password", None)
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
        messages.error(request, "Invalid credentials.")
        return redirect("login")


class LogoutView(View):
    @staticmethod
    def get(request: HttpRequest, *args, **kwargs) -> HttpResponse:
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return redirect("index")


class SignupView(View):
    @staticmethod
    def get(request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = SignupForm()
        context = {
            "title": "Sign up",
            "signup_form": form,
        }
        return render(request, "auth/signup.html", context)

    @staticmethod
    def post(request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = SignupForm(request.POST)
        username = request.POST.get("username", None)
        is_taken = User.objects.filter(username=username).first() is not None
        if is_taken:
            messages.error(request, "Please try a different username.")
        else:
            if form.is_valid():
                user = form.save()
                # NOTE: auto login not part of the test
                # login(request, user)
                messages.success(request, "Successfully signed up.")
                return redirect("login")
            else:
                messages.error(request, "Invalid credentials.")
        return redirect("signup")
