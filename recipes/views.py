from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/pages/home.html', status=201)

def recipe(request, id):
    return render(request, 'recipes/pages/home.html', status=201)
# Create your views here.