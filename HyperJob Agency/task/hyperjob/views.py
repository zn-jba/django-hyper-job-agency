from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View


class IndexView(View):
    @staticmethod
    def get(request: HttpRequest) -> HttpResponse:
        return render(request, "base.html", context={"title": "Home"})
