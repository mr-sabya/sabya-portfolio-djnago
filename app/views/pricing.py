from django.shortcuts import render

from ..models import Pricing

def index(request):
    pricings = Pricing.objects.all()

    context = {
        'pricings': pricings
    }

    return render(request, 'pricing/index.html', context)