from django.shortcuts import render
from django.http import HttpResponse

# Define the home view
def home(request):
    return HttpResponse('<h1>This is the view function "home"</h1>')