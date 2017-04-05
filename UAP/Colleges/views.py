from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.forms import ModelForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.views.generic.list import ListView
from django.utils import timezone

from .models import UniversitydataCollegedata, Statedemographics, Collegeboard, Scorecard

class IndexView(ListView):

    template_name = 'Colleges/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return [UniversitydataCollegedata.objects.filter(female__lte=98).order_by('-female')[:10],
                UniversitydataCollegedata.objects.filter(male__lte=98).order_by('-male')[:10],
                UniversitydataCollegedata.objects.order_by('-american_indian_alaskan_native')[:10]]


def uni_list(request):
    queryset_list = UniversitydataCollegedata.objects.all()

    query = request.GET.get("q")

    if query:
        queryset_list = queryset_list.filter(
            Q(university__icontains=query) |
            Q(state__location__icontains=query)
        ).distinct()

    paginator = Paginator(queryset_list, 10)  # Show 25 contacts per page
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
        "results": queryset,
        "title": "List",
        "page_request_var": page_request_var,
    }
    return render(request, "Colleges/search.html", context)


def college(request, c_id):
    keys = {
        "Asian" :"asian",
        "White" :"white",
        "Black/African-American" :"black_african_american",
        "Native Hawaiian/Pacific Islander" :"native_hawaiian_pacific_islander",
        "Hispanic/Latino" :"hispanic_latino",
        "American Indian/Alaskan Native" :"american_indian_alaskan_native",
        "Two or More Races" :"two_or_more_races",
    }

    college_data = UniversitydataCollegedata.objects.filter(id=c_id).values()[0]
    page_name = college_data['university']
    stated = college_data['state_id']

    State_demos = Statedemographics.objects.filter(location=stated).values()[0]
    Quart_dict = {}
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

            Quart_dict = {"npt41_pub": 0 , "npt42_pub": 0, "npt43_pub": 0, "npt44_pub":0, "npt45_pub":0}

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
            Quart_dict = {"npt41_priv": 0 , "npt42_priv": 0, "npt43_priv": 0, "npt44_priv":0, "npt45_priv":0}

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

    #Do Graphs
    import matplotlib
    import matplotlib.pyplot as plt
    import mpld3
    import numpy

    fig = plt.figure()
    ax = fig.add_subplot(111)
    Quarts = []
    for key, values in Quart_dict.items(): #Get Boxplots for each quartile
        LowestQuartileNPTs = Scorecard.objects.values_list(key, flat = True)
        forGraph = []
        for items in LowestQuartileNPTs:
            if items not in 'NULL':
                forGraph.append(float(items))
        Quarts.append(forGraph)

    college_specs = {} #Get college specific values
    count = 0
    for key, values in Quart_dict.items():
        count += 1
        college_specs[count] = NCES[key]

    #Finally plot
    ax.boxplot(Quarts, positions = [1,2,3,4,5])
    for cnt, val in college_specs.items():
        plt.plot(cnt,float(val), color = 'r', marker = '*', markeredgecolor = 'k', markersize=25)
    plt.xticks([1,2,3,4,5],['$30,000', '$48,000', '$75,000', '$110,000' ,'$110,000+'])
    top = 100000
    ax.set_ylim(0, top)
    graph = mpld3.fig_to_html(fig)

    #Median Graduating Income
    MGI_all = Scorecard.objects.values_list( 'md_earn_wne_p10' ,flat=True)
    Most = Scorecard.objects.filter( md_earn_wne_p10__gte = 200000)
                   # UniversitydataCollegedata.objects.filter(male__lte=98).order_by('-male')[:10],

    MGIGraph = []
    for items in MGI_all:
        if items not in ['NULL', 'PrivacySuppressed']:
            MGIGraph.append(float(items))
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    ax2.boxplot(MGIGraph)
    plt.plot(1, float(NCES['md_earn_wne_p10']), color = 'r', marker = '*', markeredgecolor = 'k', markersize=25)
    graph2 = mpld3.fig_to_html(fig2)


    return render(request, 'Colleges/detail.html',
                  {'page_name': page_name,
                   'headers':headers,
                   'data':data,
                   'financials':financials,
                   'graph': graph,
                   'Most':Most,
                   'graph2': graph2} )



