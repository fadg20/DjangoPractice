from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello World!</h1>")

def show_age(request, age):
    return HttpResponse(f"<h1>You are {age} years old!</h1>")