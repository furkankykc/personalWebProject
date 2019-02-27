from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^blog/$', views.getBlog, name='blog'),
    url(r'blog/(?P<id>\d+)/', views.getPost, name='post')
]