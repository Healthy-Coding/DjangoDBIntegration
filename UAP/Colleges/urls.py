from django.conf.urls import url

from . import views

app_name = 'Colleges'
urlpatterns = [
    url(r'^$', views.uni_list, name='search'),
    url(r'^search/$', views.college_list, name='college_list'),
    url(r'(?P<c_id>\d+)/$', views.college, name='detail'),
]