from django.conf.urls import url

from . import views

app_name = 'UniSearch'
urlpatterns = [
    #url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^$', views.AllListView.as_view(), name='allindex'),
   	#url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
   	url(r'^$', views.uni_list, name='list'),

]