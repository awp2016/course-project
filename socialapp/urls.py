from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^status/(?P<pk>\d+)/$', views.status_details, name='status_details'),
    url(r'^login', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^user-profile/(?P<pk>\d+)/$', views.user_profile, name="user_profile"),
]
