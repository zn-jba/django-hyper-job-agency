"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView

from .views import IndexView
from .views import LoginView
from .views import LogoutView
from .views import SignupView

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("", IndexView.as_view(), name="index"),
    path("home", RedirectView.as_view(url=""), name="home"),
    path("home/", RedirectView.as_view(url="")),

    path("login", LoginView.as_view(), name="login"),
    path("login/", RedirectView.as_view(url="/login")),

    path("logout", LogoutView.as_view(), name="logout"),
    path("logout/", RedirectView.as_view(url="/logout")),

    path("signup", SignupView.as_view(), name="signup"),
    path("signup/", RedirectView.as_view(url="/signup")),

    path("resumes/", RedirectView.as_view(url="/resumes")),
    path("vacancies/", RedirectView.as_view(url="/vacancies")),

    path("resumes", include("resume.urls")),
    path("vacancies", include("vacancy.urls")),
]

urlpatterns += static(settings.STATIC_URL)
