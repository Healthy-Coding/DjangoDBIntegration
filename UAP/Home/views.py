from django.shortcuts import render
from .forms import ContactForm

def handler404(request):
    return render(request, '404.html', status=400)


def home(request):
    return render(request, 'home.html', {'nbar': 'home'})


def about(request):
    return render(request, 'about.html', {'nbar': 'about'})


def contact(request):
    form = ContactForm()
    return render(request, 'contact.html', {'nbar': 'contact', 'form': form})

