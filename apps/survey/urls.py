from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^/process$', views.getData),
    url(r'^result$', views.displayResult),
    url(r'^back$', views.goBack),
]
