from django.urls import path

from .views import ResumesView

app_name = "resume"
urlpatterns = [
    path("resumes", ResumesView.as_view(), name="resumes"),
]
