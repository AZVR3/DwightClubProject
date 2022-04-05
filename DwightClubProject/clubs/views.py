from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    context = {"name": "student"}
    return render(request, "clubs/home.html", context)