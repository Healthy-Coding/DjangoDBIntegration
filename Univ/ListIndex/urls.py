from django.conf.urls import url

from . import views

app_name = 'ListIndex'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
   # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

]