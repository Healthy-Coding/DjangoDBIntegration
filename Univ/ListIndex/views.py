from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.forms import ModelForm


from .models import UniversitydataCollegedata, Statedemographics

class IndexView(generic.ListView):
    template_name = 'ListIndex/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
	    """Return the last five published questions."""
	    return [UniversitydataCollegedata.objects.filter(female__lte=98).order_by('-female')[:10], UniversitydataCollegedata.objects.filter(male__lte = 98).order_by('-male')[:10], UniversitydataCollegedata.objects.order_by('-american_indian_alaskan_native')[:10]]


def index(request):
	queryset_list = UniversitydataCollegedata.objects.all()
	q2 = Statedemographics.object.all()
	stateInfo = {}

	latest_question_list= [UniversitydataCollegedata.objects.filter(female__lte=98).order_by('-female')[:10], UniversitydataCollegedata.objects.filter(male__lte = 98).order_by('-male')[:10], UniversitydataCollegedata.objects.order_by('-american_indian_alaskan_native')[:10]]
	
	for objects in latest_question_list: #Match state data
		stateInfo[objects.university] = q2.objects.filter(objects.state)

	for objects in latest_question_list[0]:
		objects = 
	latest_question_list.append
	context = {'latest_question_list':latest_question_list}

	query =request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(university__icontains=query)

	return render(request, 'ListIndex/index.html', context, queryset_list)

def detail(request, question_id):
    question = UniversitydataCollegedata.objects.filter(id=question_id).values()[0]
    return render(request, 'ListIndex/detail.html', {'question': question})


# class DetailView(generic.DetailView):
# 	model = UniversitydataCollegedata
# 	template_name = 'ListIndex/detail.html'
# 	context_object_name = 'latest_question_list'


# 	def detail(request, object_id):
# 	   thing = UniversitydataCollegedata.objects.filter(id=object_id).values()
# 	   return render_to_response('ListIndex/detail.html', {'thing': thing})

# 	def show(request, object_id):
# 	   thing = UniversitydataCollegedata.objects.filter(id=object_id).values()
# 	   return render_to_response('ListIndex/detail.html', {'thing': thing})
	#context_object_name = 'latest_question_list'