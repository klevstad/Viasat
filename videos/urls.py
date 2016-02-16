from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^videos', views.videos, name='videos'),
	url(r'^(?P<object_id>[0-9]+)/$', views.detail, name='detail'),
]