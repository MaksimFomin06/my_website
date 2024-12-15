from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    context: dict = {
        "title": "Главная"
    }
    return render(request, "my_site/index.html", context)