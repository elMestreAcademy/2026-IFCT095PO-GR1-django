# from django.shortcuts import render <- Esto seria lo normal

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
