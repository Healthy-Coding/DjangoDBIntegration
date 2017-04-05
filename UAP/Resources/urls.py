from django.conf.urls import url

from . import views

app_name = 'Resources'
urlpatterns = [
    url(r'^search/$', views.post_list, name='search'),
    url(r'(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='detail'),
]