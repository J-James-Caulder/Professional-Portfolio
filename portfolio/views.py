from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Future, Finished, Recording

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':projects})

def FinishedProjects(request):
    finished = Finished.objects.all()
    return render(request, 'portfolio/FinishedProjects.html', {'finished':finished})

def all_blogs(request):
    return render(request, 'blog/all_blogs.html')

def UpcomingProjects(request):
    future = Future.objects.all()
    return render(request, 'portfolio/UpcomingProjects.html', {'future':future})

def Contact(request):
    return render(request, 'portfolio/Contact.html')

def Demo(request):
    recordings = Recording.objects.all()
    return render(request, 'portfolio/Demo.html', {'recordings':recordings})
