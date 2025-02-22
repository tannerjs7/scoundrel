from django.shortcuts import render
from .models import Card


def index(request):
    cards = Card.objects.all()
    context = {
        'cards': cards,
        'hp': 20,
        'room': 1
    }
    return render(request, 'scoundrel/index.html', context)