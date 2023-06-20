from django.shortcuts import render

from ..models import Project, Service, Skill, Education

def index(request):
    projects = Project.objects.all()
    services = Service.objects.all()[:3]
    skills = Skill.objects.all()
    educations = Education.objects.all()

    context = {
        'projects': projects,
        'services': services,
        'skills': skills,
        'educations': educations,
    }

    return render(request, 'home/index.html', context)