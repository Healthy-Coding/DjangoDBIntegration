from django.shortcuts import render


def handler404(request):
    return render(request, '404.html', status=400)


def home(request):
    return render(request, 'home.html', {'nbar': 'home'})


def about(request):
    return render(request, 'about.html', {'nbar': 'about'})
