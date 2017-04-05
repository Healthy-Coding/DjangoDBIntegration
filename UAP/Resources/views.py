from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormMixin

from .forms import PostSearchForm

from django.views import generic




class PostListView(generic.ListView):
    model = Post


class PostSearchListView(PostListView):
    paginate_by = 10
    template_name = 'resources_search.html'

    def get_queryset(self):
        result = super(PostListView, self).get_queryset()

        query = self.request.GET.get('q')

        if query:
            result = result.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()

        return result


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'Resources/detail.html'


def post_list(request):
    queryset_list = Post.objects.all()

    if len(queryset_list) == 0:
        return render(request, "Resources/search.html", {"results": None,
                                                         "title": "List",
                                                         "page_request_var": "page"})

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()

    paginator = Paginator(queryset_list, 10)
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
    return render(request, "Resources/search.html", context)


