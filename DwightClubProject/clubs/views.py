from django.shortcuts import render
from django.http import HttpResponse
from clubs.forms import UserForm

clubs = [
    {'clubname': 'entrepeneurship'},
    {''}
]

# Create your views here.
def home(request):
    context = {"name": "Student", "clubs": clubs}
    return render(request, "clubs/home.html", context)

def feed(request):
    context = {"name": "Student", "clubs": clubs}
    return render(request, "clubs/feed.html", context)

def club(request):
    context = {"name": "Student", "clubs": clubs}
    return render(request, "clubs/club.html", context)

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return rediret('home')
    else:
        form = UserForm()

    return render(request, 'register.html', {'form':form})
    