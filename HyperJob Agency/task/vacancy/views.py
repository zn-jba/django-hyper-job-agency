from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import HttpRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import View

from .forms import VacancyForm
from .models import Vacancy


class VacancyView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:

        context = {
            "title": "Vacancies",
            "vacancies": Vacancy.objects.all(),
        }

        return render(request, "vacancy/index.html", context)


class NewVacancyView(View):
    @staticmethod
    def get(request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if not request.user.is_staff:
            return redirect("home")

        form = VacancyForm()
        context = {
            "title": "Add Vacancy",
            "vacancy_form": form
        }

        return render(request, "create.html", context)

    @staticmethod
    def post(request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = VacancyForm(request.POST)
        if request.user.is_staff and form.is_valid():
            description = form.cleaned_data.get("description", None)
            Vacancy.objects.create(author=request.user, description=description)
            messages.info(request, "Vacancy added.")
            return redirect("home")
        # messages.error(request, "Something went wrong with adding a vacancy.")
        return HttpResponseForbidden()
