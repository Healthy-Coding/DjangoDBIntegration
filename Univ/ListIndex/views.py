from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Georgialargest15

class IndexView(generic.ListView):
    template_name = 'ListIndex/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
	    """Return the last five published questions."""
	    return [Georgialargest15.objects.order_by('-women')[:10], Georgialargest15.objects.order_by('-men')[:10], Georgialargest15.objects.order_by('-amer_indian')[:10]]


class DetailView(generic.DetailView):
	model = Georgialargest15
	template_name = 'ListIndex/detail.html'

	# def detail(request, id):
 #    	college = get_object_or_404(Georgialargest15, pk=id)
 #    	return render(request, 'ListIndex/detail.html', {'college': college})