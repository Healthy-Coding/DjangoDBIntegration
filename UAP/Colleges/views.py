from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.db.models import Q
from .models import UniversitydataCollegedata, Statedemographics, Collegeboard, Scorecard, Collegepictures
from .forms import SimpleSearchForm


def flag_page(request, c_id):
    return render(request, "Colleges/flag_page.html", {'flag': c_id})


def search(request):
    if request.method == "POST":
        form = SimpleSearchForm(request.POST)
        if form.is_valid():
            queryset_list = UniversitydataCollegedata.objects.all()

            query = form.cleaned_data['query']
            paginate_by = int(form.cleaned_data['paginate_by'])

            if query != "":
                 queryset_list = queryset_list.filter(
                     Q(university__icontains=query)
                 ).distinct()

            if queryset_list.count() > paginate_by:
                page = request.GET.get("page")
                paginator = Paginator(queryset_list, paginate_by)

                pagination = True
                try:
                    queryset_list = paginator.page(page)
                except PageNotAnInteger:
                    # If page is not an integer, deliver first page.
                    queryset_list = paginator.page(1)
                except EmptyPage:
                    # If page is out of range (e.g. 9999), deliver last page of results.
                    queryset_list = paginator.page(paginator.num_pages)
            else:
                pagination = False

            return render(request,"Colleges/search.html", {'form': form,
                                                           'results': queryset_list,
                                                           'pagination': pagination,
                                                           'nbar': 'colleges'})

    else:
        form = SimpleSearchForm()
        return render(request, "Colleges/search.html", {'form': form, 'results': None, 'nbar': 'colleges'})


def uni_list(request):
    queryset_list = UniversitydataCollegedata.objects.all()
    query = request.GET.get("q")

    if query is not None:
        queryset_list = queryset_list.filter(
            Q(university__icontains=query) |
            Q(state__location__icontains=query)
        ).distinct()

        page_request_var = "page"
        paginate_by = 10

        if queryset_list.count() > paginate_by:
            pagination = True
            paginator = Paginator(queryset_list, 10)
            page = request.GET.get(page_request_var)
            try:
                queryset = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                queryset = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                queryset = paginator.page(paginator.num_pages)
        else:
            queryset = queryset_list
            pagination = False

        context = {
            "nbar": "colleges",
            "results": queryset,
            "title": "List",
            "page_request_var": page_request_var,
            "pagination": pagination
        }

        return render(request, "Colleges/search.html", context)

    else:
        context = {
            "nbar": "colleges",
            "results": None,
            "title": "List",
            "page_request_var": None,
        }

        return render(request, "Colleges/search.html", context)


def access_db(key, db):
    try:
        return db[key]
    except KeyError:
        return "*"


def college(request, c_id):
    db_keys = ['asian', 'white', 'black_african_american',
               'native_hawaiian_pacific_islander', 'hispanic_latino',
               'american_indian_alaskan_native', 'multi_race']

    keys = {
        "Asian": "asian",
        "White": "white",
        "Black/African-American": "black_african_american",
        "Native Hawaiian/Pacific Islander": "native_hawaiian_pacific_islander",
        "Hispanic/Latino": "hispanic_latino",
        "American Indian/Alaskan Native": "american_indian_alaskan_native",
        "Two or More Races": "multi_race",
    }

    college_data = UniversitydataCollegedata.objects.filter(id=c_id).values()[0]

    page_name = college_data['university']
    state = college_data['state_id']
    city = college_data['city']

    try:
        college_pictures = Collegepictures.objects.filter(university_name=page_name).values()[0]
    except IndexError:
        college_pictures = "#"

    State_demos = Statedemographics.objects.filter(location=state).values()[0]
    Quart_dict = {}
    try:
        college_board = Collegeboard.objects.filter(
            university=page_name).values()[0]
        NCES = Scorecard.objects.filter(instnm=page_name).values()[0]

        financial_percent = {
            "Pell Grant Recipients": "pctpell",
            "Federal Loan Recipients": "pctfloan",
            "4 Year Retention Rate": "ret_ft4",
            "Completion Within 1.0x-1.5x of Expected Time": "c150_4_pooled_supp",
            "Percent of Graduating Students Earning Over $25k": "gt_25k_p6",
        }

        if NCES['control'] == 1:
            financial_dollars = {
                "Median Graduating Income": "md_earn_wne_p10",
                "Median Graduating Debt": "grad_debt_mdn_supp",
                "Average Net Price for $0-$30,000": "npt41_pub",
                "Average Net Price for $30,001-$48,000": "npt42_pub",
                "Average Net Price for $48,001-$75,000": "npt43_pub",
                "Average Net Price for $75,001-$110,000": "npt44_pub",
                "Average Net Price for $110,001+": "npt45_pub"
            }

            Quart_dict = {"npt41_pub": 0, "npt42_pub": 0,
                          "npt43_pub": 0, "npt44_pub": 0, "npt45_pub": 0}

        if NCES['control'] == 2:
            financial_dollars = {
                "Median Graduating Income": "md_earn_wne_p10",
                "Median Graduating Debt": "grad_debt_mdn_supp",
                "Average Net Price for $0-$30,000": "npt41_priv",
                "Average Net Price for $30,001-$48,000": "npt42_priv",
                "Average Net Price for $48,001-$75,000": "npt43_priv",
                "Average Net Price for $75,001-$110,000": "npt44_priv",
                "Average Net Price for $110,001+": "npt45_priv"
            }
            if False:
                financial_percent = {
                    "Pell Grant Recipients": "pctpell",
                    "Federal Loan Recipients": "pctfloan",
                    "4 Year Retention Rate": "ret_ft4",
                    "Completion Within 1.0x-1.5x of Expected Time": "c150_4_pooled_supp",
                    "Percent of Graduating Students Earning Over $25k": "gt_25k_p6",
                }
            Quart_dict = {"npt41_priv": 0, "npt42_priv": 0,
                          "npt43_priv": 0, "npt44_priv": 0, "npt45_priv": 0}


        dollars = {}
        for display, db_key in financial_dollars.items():
            dollars[display] = int(NCES[db_key])

        percent = {}
        for display, db_key in financial_percent.items():
            percent[display] = float(NCES[db_key][0:5])

    except IndexError:
        NCES = {}
        financials = {}
        college_board = {}

    headers = ["Metric", "College Data", "College Board", "NCES", "State Demographics"]
    data = {}

    for display, db_key in keys.items():
        data[display] = [access_db(db_key, college_data),
                         access_db(db_key, college_board),
                         access_db(db_key, NCES),
                         access_db(db_key, State_demos)]

    if False:
        # Do Graphs
        import matplotlib
        import matplotlib.pyplot as plt
        import mpld3
        import numpy

        fig = plt.figure()
        ax = fig.add_subplot(111)
        Quarts = []
        for key, values in Quart_dict.items():  # Get Boxplots for each quartile
            LowestQuartileNPTs = Scorecard.objects.values_list(key, flat=True)
            forGraph = []
            for items in LowestQuartileNPTs:
                if items not in 'NULL':
                    forGraph.append(float(items))
            Quarts.append(forGraph)

        college_specs = {}  # Get college specific values
        count = 0
        for key, values in Quart_dict.items():
            count += 1
            college_specs[count] = NCES[key]

        # Finally plot
        ax.boxplot(Quarts, positions=[1, 2, 3, 4, 5])
        for cnt, val in college_specs.items():
            plt.plot(cnt, float(val), color='r', marker='*',
                     markeredgecolor='k', markersize=25)
        plt.xticks([1, 2, 3, 4, 5], ['$30,000', '$48,000',
                                     '$75,000', '$110,000', '$110,000+'])
        top = 100000
        ax.set_ylim(0, top)
        graph = mpld3.fig_to_html(fig)

        # Median Graduating Income
        MGI_all = Scorecard.objects.values_list('md_earn_wne_p10', flat=True)
        Most = Scorecard.objects.filter(md_earn_wne_p10__gte=200000)
        # UniversitydataCollegedata.objects.filter(male__lte=98).order_by('-male')[:10],

        MGIGraph = []
        for items in MGI_all:
            if items not in ['NULL', 'PrivacySuppressed']:
                MGIGraph.append(float(items))

        fig2 = plt.figure()
        ax2 = fig2.add_subplot(111)
        ax2.boxplot(MGIGraph)
        plt.plot(1, float(NCES['md_earn_wne_p10']), color='r',
                 marker='*', markeredgecolor='k', markersize=25)
        graph2 = mpld3.fig_to_html(fig2)

    google_graph = []
    google_graph.append(['Demographics', 'College Data',
                         'CollegeBoard', 'NCES', 'State Demographics'])

    for k, v in data.items():
        if v[1]==None:
            v[1] = 0
        if v[2]==None:
            v[2] = 0
        if v[3]=='N/A' or v[3]==None:
            v[3] = 0
        google_graph.append([k,
                float(v[0])*.01, 
                float(v[1]), 
                float(v[2]),
                float(v[3]) ])

    #print"google_graph", google_graph
    return render(request, 'Colleges/detail.html',
                  {'nbar': None,
                   'page_name': page_name,
                   'city': city,
                   'state': state,
                   'headers': headers,
                   'data': data,
                   'dollars': dollars,
                   'percent': percent,
                   'id': c_id,
                   'college_pictures': college_pictures,
                   'google_graph': google_graph})
                   #'graph': graph,
                   #'Most': Most,
                   #'graph2': graph2})
