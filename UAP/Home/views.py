from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
from .models import Contact
from datetime import datetime
import random

def handler404(request):
    return render(request, '404.html', status=400)


def home(request):
    startURL = "/static/assets/img/" 
    Pics = ["bowen-quad.jpg", "Brown.jpg", "College1.jpg","College2.jpg","College3.jpg","College4.jpg","College5.jpg","College6.jpg","College7.jpg","Penn.jpg"]
    selectedPics = []
    while len(selectedPics) < 4:
        pic = random.choice(Pics)
        if startURL+pic not in selectedPics:
            selectedPics.append(startURL+pic)
    print selectedPics
    return render(request, 'home.html', {'nbar': 'home', 'selectedPics':selectedPics})


def about(request):
    return render(request, 'about.html', {'nbar': 'about'})


def thanks(request):
    return render(request, 'thanks.html')

def citation(request):
    return render(request, 'citation.html')


def contact(request):
    # Template sends back post request -- bind form data to a new Contact model
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # TODO: Contact object needs to exist in the database
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['sender']
            c = Contact(subject=subject, content=message, sender=email, timesent=datetime.utcnow())
            c.save()
            return HttpResponseRedirect('/thanks/')

    # Get request means view renders a blank form
    else:
        return render(request, 'contact.html', {'nbar': 'contact', 'form': ContactForm()})
