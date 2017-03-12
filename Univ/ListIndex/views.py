from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import UniversitydataCollegedata

class IndexView(generic.ListView):
    template_name = 'ListIndex/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
	    """Return the last five published questions."""
	    return [UniversitydataCollegedata.objects.order_by('-female')[:10], UniversitydataCollegedata.objects.order_by('-male')[:10], UniversitydataCollegedata.objects.order_by('-american_indian_alaskan_native')[:10]]


class DetailView(generic.DetailView):
	model = UniversitydataCollegedata
	template_name = 'ListIndex/detail.html'

	# def detail(request, id):
 #    	college = get_object_or_404(Georgialargest15, pk=id)
 #    	return render(request, 'ListIndex/detail.html', {'college': college})