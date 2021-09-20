from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from .forms import ResumeForm
from .models import Resume


class ResumesView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:

        context = {
            "title": "Resumes",
            "resumes": Resume.objects.all(),
        }

        return render(request, "resume/index.html", context)


class NewResumeView(View):
    @staticmethod
    def get(request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = ResumeForm()
        context = {
            "title": "Add Resume",
            "resume_form": form
        }
        return render(request, "create.html", context)

    @staticmethod
    def post(request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = ResumeForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data.get("description", None)
            Resume.objects.create(author=request.user, description=description)
            messages.info(request, "Resume added.")
            return redirect("home")
        # messages.error(request, "Something went wrong with adding a resume.")
        return HttpResponseForbidden()
