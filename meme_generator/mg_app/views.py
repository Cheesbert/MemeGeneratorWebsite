from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def mg_app(request):
    return render(request, "mg_home.html")

def create_meme(request):
    return render(request, "templates.create_meme.html")


