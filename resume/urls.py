from django.urls import path
from django.views.generic import RedirectView

from .views import NewResumeView
from .views import ResumesView

app_name = "resume"
urlpatterns = [
    path("resumes", ResumesView.as_view(), name="resumes"),
    path("resumes/", RedirectView.as_view(url="/resumes")),

    path("resume/new", NewResumeView.as_view(), name="new"),
    path("resume/new/", RedirectView.as_view(url="/resume/new")),
]
