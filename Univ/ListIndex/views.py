from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.forms import ModelForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import UniversitydataCollegedata, Statedemographics, Collegeboard, Scorecard


class IndexView(generic.ListView):
    template_name = 'ListIndex/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return [UniversitydataCollegedata.objects.filter(female__lte=98).order_by('-female')[:10],
                UniversitydataCollegedata.objects.filter(male__lte=98).order_by('-male')[:10],
                UniversitydataCollegedata.objects.order_by('-american_indian_alaskan_native')[:10]]


def index(request):
    stateDemo = {}
    latest_question_list = [UniversitydataCollegedata.objects.filter(female__lte=98).order_by('-female')[:10],
                            UniversitydataCollegedata.objects.filter(male__lte=98).order_by('-male')[:10],
                            UniversitydataCollegedata.objects.order_by('-american_indian_alaskan_native')[:10]]

    for quer in latest_question_list:
        for Univ in quer:
            stateDemo[Univ.university] = UniversitydataCollegedata.objects.select_related()

    latest_question_list.append(stateDemo)
    context = {'latest_question_list': latest_question_list}

    return render(request, 'ListIndex/index.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')



def uni_list(request):
    queryset_list = UniversitydataCollegedata.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(university__icontains=query) |
            Q(state__location__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 8)  # Show 25 contacts per page
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
    return render(request, "search/list.html", context)


def detail(request, question_id):
    keys = {
        "Asian" :"asian",
        "White" :"white",
        "Black/African-American" :"black_african_american",
        "Native Hawaiian/Pacific Islander" :"native_hawaiian_pacific_islander",
        "Hispanic/Latino" :"hispanic_latino",
        "American Indian/Alaskan Native" :"american_indian_alaskan_native",
        "Two or More Races" :"two_or_more_races",
    }

    college_data = UniversitydataCollegedata.objects.filter(id=question_id).values()[0]
    page_name = college_data['university']
    stated = college_data['state_id']

    State_demos = Statedemographics.objects.filter(location=stated).values()[0]
    try:
        college_board = Collegeboard.objects.filter(university=page_name).values()[0]
        NCES = Scorecard.objects.filter(instnm = page_name).values()[0]

        if NCES['control'] == 1:
            financial_dict = {
                "Median Graduating Income" : "md_earn_wne_p10",
                "Median Graduating Debt": "grad_debt_mdn_supp",
                "Percent Pell": "pctpell",
                "Percent Federal Loan": "pctfloan",
                "4 Year Retention": "ret_ft4",
                "Completion Within 1.0x-1.5x of Expected Time": "c150_4_pooled_supp",
                "Percent of Graduating Students Earning Over $25k": "gt_25k_p6",
                "Average Net Price for $0-$30,000": "npt41_pub",
                "Average Net Price for $30,001-$48,000": "npt42_pub",
                "Average Net Price for $48,001-$75,000": "npt43_pub",
                "Average Net Price for $75,001-$110,000": "npt44_pub",
                "Average Net Price for $110,001+": "npt45_pub"
            }

        if NCES['control'] == 2:
            financial_dict = {
                "Median Graduating Income" : "md_earn_wne_p10",
                "Median Graduating Debt": "grad_debt_mdn_supp",
                "Percent Pell": "pctpell",
                "Percent Federal Loan": "pctfloan",
                "4 Year Retention": "ret_ft4",
                "Completion Within 1.0x-1.5x of Expected Time": "c150_4_pooled_supp",
                "Percent of Graduating Students Earning Over $25k": "gt_25k_p6",
                "Average Net Price for $0-$30,000": "npt41_priv",
                "Average Net Price for $30,001-$48,000": "npt42_priv",
                "Average Net Price for $48,001-$75,000": "npt43_priv",
                "Average Net Price for $75,001-$110,000": "npt44_priv",
                "Average Net Price for $110,001+": "npt45_priv"
            }

        financials = {}
        for display, db_key in financial_dict.items():
            financials[display] = NCES[db_key]

    except IndexError:
        financials = {}
        college_board ={}

    headers = ["Metric", "College Data", "College Board", "National Center for Education Statistics", "State Demographics"]
    data = {}
    for display, db_key in keys.items():
        data[display] = [college_data[db_key], college_board[db_key], NCES[db_key], State_demos[db_key]]



    return render(request, 'ListIndex/detail.html',
                  {'page_name': page_name,
                   'headers':headers,
                   'data':data,
                   'financials':financials})



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
    # context_object_name = 'latest_question_list'
