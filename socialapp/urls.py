from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.StatusListView.as_view(), name='index'),
    url(r'^status/(?P<pk>\d+)/$', views.status_details, name='status_details'),
    url(r'^login', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^user-profile/(?P<pk>\d+)/$', views.user_profile,
        name="user_profile"),
    url(r'^user-profile/(?P<pk>\d+)/edit/$', views.edit_user_profile,
        name="edit_user_profile"),
    url(r'^status/(?P<pk>\d+)/edit/$', views.StatusUpdate.as_view(),
        name='update_status'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
