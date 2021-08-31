from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Finished, Future

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})

def FinishedProjects(request):
    finished = Finished.objects.all()
    return render(request, 'portfolio/FinishedProjects.html')

def all_blogs(request):
    return render(request, 'blog/all_blogs.html')

def UpcomingProjects(request):
    future = Future.objects.all()
    return render(request, 'portfolio/UpcomingProjects.html')

def Contact(request):
    return render(request, 'portfolio/Contact.html')

def Demo(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/demo.html')
