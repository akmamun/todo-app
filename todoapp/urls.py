from django.conf.urls import url,include
from django.contrib import admin
from todoapp.views import index,add,details,login,register

urlpatterns = [
    url(r'^$', index,name="index"),
    url(r'^add', add, name="add"),
    url(r'^details/(?P<id>\d+)/$', details, name="details"),
    url(r'^login/$', login, name='login'),
    url(r'^register/$', register, name='register'),


]
