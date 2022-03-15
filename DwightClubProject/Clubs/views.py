from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calendar(request):
    return HttpResponse("Hello, you are at the calendar page.")