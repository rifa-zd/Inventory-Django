from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This is the index page.")

def staff(request):
    return HttpResponse("This is staff page.")
