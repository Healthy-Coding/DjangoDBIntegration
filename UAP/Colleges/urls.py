from django.conf.urls import url

from . import views

app_name = 'Colleges'
urlpatterns = [
    url(r'^(?P<c_id>[0-9]+)/flag/$', views.flag_page, name='flag_page'),
    url(r'^$', views.search, name='search'),
    url(r'(?P<c_id>\d+)/$', views.college, name='detail'),
]
