from django.shortcuts import render
from ..models import Pricing, Order

def index(request, slug):
    pricing = Pricing.objects.get(slug=slug)
    
    return render(request, 'about/index.html')