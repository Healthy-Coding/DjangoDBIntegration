from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
from .models import Contact
from datetime import datetime


def handler404(request):
    return render(request, '404.html', status=400)


def home(request):
    return render(request, 'home.html', {'nbar': 'home'})


def about(request):
    return render(request, 'about.html', {'nbar': 'about'})


def thanks(request):
    return render(request, 'thanks.html')


def contact(request):
    # Template sends back post request -- bind form data to a new Contact model
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # TODO: Contact object needs to exist in the database
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['sender']
            c = Contact(subject=subject, content=message, sender=email, time_sent=datetime.utcnow())
            # c.save()
            return HttpResponseRedirect('/thanks/')

    # Get request means view renders a blank form
    else:
        return render(request, 'contact.html', {'nbar': 'contact', 'form': ContactForm()})
