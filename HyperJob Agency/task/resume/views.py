from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from .models import Resume


class ResumesView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:

        context = {
            "title": "Resumes",
            "resumes": Resume.objects.all(),
        }

        return render(request, "resume/index.html", context)
