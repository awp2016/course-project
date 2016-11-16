from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^status/(?P<pk>\d+)/$', views.status_details, name='status_details'),
]
