from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from .models import Vacancy


class VacancyView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:

        context = {
            "title": "Vacancies",
            "vacancies": Vacancy.objects.all(),
        }

        return render(request, "vacancy/index.html", context)
