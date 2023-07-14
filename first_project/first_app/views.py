from django.shortcuts import render
from django.http import HttpResponse
from .forms import SearchForm, TestForm, PostModelForm

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def show_age(request, age):
    return HttpResponse(f"<h1>You are {age} years old!</h1>")

def forms(request):
    form = PostModelForm(request.POST or None)
    data = "None"
    text = "None"
    if form.is_valid():
        data = form.cleaned_data
        text = form.cleaned_data.get("text")
    return render(request, 'first_app/forms.html', {'form': form, 'data': data, 'text': text})