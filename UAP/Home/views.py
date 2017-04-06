from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm


def handler404(request):
    return render(request, '404.html', status=400)


def home(request):
    return render(request, 'home.html', {'nbar': 'home'})


def about(request):
    return render(request, 'about.html', {'nbar': 'about'})


def thanks(request):
    return render(request, 'thanks.html')


def contact(request):
    # Need to process the data
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # TODO: Add what is done with the form here

            return HttpResponseRedirect('/thanks/')
            #return

    # Need to provide form for user input
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'nbar': 'contact', 'form': form})
