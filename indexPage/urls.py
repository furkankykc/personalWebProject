from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.runIndex, name='post_list'),
    url(r'refresh', views.refreshDB, name='refresh')
]