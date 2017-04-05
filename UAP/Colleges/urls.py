from django.conf.urls import url

from . import views

app_name = 'Colleges'
urlpatterns = [
    url(r'^search/$', views.uni_list, name='search'),
    url(r'(?P<c_id>\d+)/$', views.college, name='detail'),
]