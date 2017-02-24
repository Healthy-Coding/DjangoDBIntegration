from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Georgia

class IndexView(generic.ListView):
    template_name = 'ListIndex/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
	    """Return the last five published questions."""
	    return [Georgia.objects.order_by('-women')[:10], Georgia.objects.order_by('-men')[:10], Georgia.objects.order_by('-amer_indian')[:10]]