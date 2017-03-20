#For UniSearch
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.forms import ModelForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


from .models import UniversitydataCollegedata, Statedemographics

class IndexView(generic.ListView):
	model = UniversitydataCollegedata
	template_name = 'ListIndex/index.html'

	def get_queryset(self):
		female = UniversitydataCollegedata.objects.filter(female__lte=98).order_by('-female')[:10]
		male = UniversitydataCollegedata.objects.filter(male__lte = 98).order_by('-male')[:10]
		hispanic = UniversitydataCollegedata.objects.order_by('-hispanic_latino')[:10]
		indian = UniversitydataCollegedata.objects.order_by('-american_indian_alaskan_native')[:10]

		context = {'female': female , 'male': male, 'hispanic': hispanic, 'indian': indian }
		context_object_name = context

		return context

def index(request):
	female = UniversitydataCollegedata.objects.filter(female__lte=98).order_by('-female')[:10]
	male = UniversitydataCollegedata.objects.filter(male__lte = 98).order_by('-male')[:10]
	hispanic = UniversitydataCollegedata.objects.order_by('-hispanic_latino')[:10]
	indian = UniversitydataCollegedata.objects.order_by('-american_indian_alaskan_native')[:10]

	context = {'female': female , 'male': male, 'hispanic': hispanic, 'indian': indian }

	return render(request, 'ListIndex/index.html', context)

def detail(request, question_id):
    question = UniversitydataCollegedata.objects.filter(id=question_id).values()[0]
    return render(request, 'ListIndex/detail.html', {'question': question})

def uni_list(request):
	queryset_list = UniversitydataCollegedata.objects.all() 
	
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(university__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 8) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	context = {
		"object_list": queryset, 
		"title": "List",
		"page_request_var": page_request_var,
	}
	return render(request, "post_list.html", context)
