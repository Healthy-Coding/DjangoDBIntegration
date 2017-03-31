from django.conf.urls import url
from django.views.generic import RedirectView

from . import views

app_name = 'ListIndex'
urlpatterns = [
    #url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^$', views.index, name='index'),
    #url(r'^(?P<c_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.home, name='home'),
    url(r'^home/', views.home, name='home'),
    url(r'^search/', views.search, name='search'),
    url(r'^about/', views.about, name='about'),
    url(r'^college/(?P<c_id>[0-9]+)/$', views.college, name='college')
]