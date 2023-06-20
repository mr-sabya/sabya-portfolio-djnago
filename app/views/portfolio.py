from django.shortcuts import render
from ..models import Project

def index(request):
    return render(request, 'portfolio/index.html')



def show(request, slug):
    project = Project.objects.get(slug = slug)

    context = {
        'project': project
    }

    return render(request, 'portfolio/show.html', context)