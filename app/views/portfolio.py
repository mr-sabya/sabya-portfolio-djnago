from django.shortcuts import render
from ..models import Project

def index(request):
    projects = Project.objects.all()

    context = {
        'projects': projects,
    }
    return render(request, 'portfolio/index.html', context)



def show(request, slug):
    project = Project.objects.get(slug = slug)

    context = {
        'project': project
    }

    return render(request, 'portfolio/show.html', context)