from django.conf.urls import url

from . import views

app_name = 'Resources'
urlpatterns = [
    url(r'^$', views.post_list, name='search'),
    url(r'^(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name='detail'),
]