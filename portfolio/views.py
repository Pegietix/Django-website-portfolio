from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "portfolio/index.html")


def technologies(request):
    return render(request, "portfolio/technologies.html")


def projects(request):
    return render(request, "portfolio/projects.html")


def hobbies(request):
    return render(request, "portfolio/hobbies.html")


def gmail(request):
    return render(request, "portfolio/gmail.html")
