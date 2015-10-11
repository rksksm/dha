from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from . import views

urlpatterns = [
		url(r'^$',views.index, name = 'index'),
		url(r'^r',views.r, name = 'r'),
		url(r'^f',views.f, name = 'f'),
		url(r'^m',views.m, name = 'm'),
		url(r'^corp',views.corp, name = 'corp'),
		url(r'^const',views.const, name = 'const'),
		url(r'^b',views.b, name = 'b'),
		]


