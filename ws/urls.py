# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^upload/$', views.MultiFileUploadView.as_view(), name='upload'),
	url(r'^profile-preview/(?P<id>[\w\-]+)/$', views.PortadaPreviewView.as_view(), name='profile-preview'),
]

