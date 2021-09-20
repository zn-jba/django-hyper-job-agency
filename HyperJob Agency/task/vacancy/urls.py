from django.urls import path
from django.views.generic import RedirectView

from .views import NewVacancyView
from .views import VacancyView

app_name = "vacancy"
urlpatterns = [
    path("vacancies", VacancyView.as_view(), name="vacancies"),
    path("vacancies/", RedirectView.as_view(url="/vacancies")),

    path("vacancy/new", NewVacancyView.as_view(), name="new"),
    path("vacancy/new/", RedirectView.as_view(url="/vacancy/new")),
]
