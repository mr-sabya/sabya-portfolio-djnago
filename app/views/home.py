from django.shortcuts import render

from ..models import *

def index(request):
    projects = Project.objects.all()
    services = Service.objects.all()[:3]
    skills = Skill.objects.all()
    educations = Education.objects.all()
    info = Info.objects.get(id = 1)
    brands = Brand.objects.all()
    feedbacks = Feedback.objects.all()
    blogs = Blog.objects.all()[:3]

    context = {
        'projects': projects,
        'services': services,
        'skills': skills,
        'info': info,
        'educations': educations,
        'brands': brands,
        'feedbacks': feedbacks,
        'blogs': blogs
    }

    return render(request, 'home/index.html', context)