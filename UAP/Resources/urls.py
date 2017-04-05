from django.conf.urls import url

from . import views

app_name = 'Resources'
urlpatterns = [
    url(r'^search/$', views.post_list, name='search'),
    url(r'^(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name='detail'),
    #url(r'^create/$', post_create),
    #url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    #url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    #url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),

    #url(r'^posts/$', "<appname>.views.<function_name>"),
]