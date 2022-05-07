from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

def optout(request):
       return redirect("http://stackoverflow.com/")