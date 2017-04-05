from django.conf.urls import url

from . import views

app_name = 'Home'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),

]