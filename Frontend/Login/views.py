from django.http import HttpResponse
from django.shortcuts import render


def Login(request):
    return render(request, "index.html", {"nome": "Daniel"})

