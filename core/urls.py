from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login,logout
from . import views

app_name = 'core'

urlpatterns = [
    #homepage
    url(r'^$',views.index,name='index'),
    #profile_realted
    url(r'^register/$',views.register,name='reg'),
    url(r'accounts/profile/$',views.account,name='account'),
    url(r'login/$',login,{'template_name':'core/login.html'},name='login'),
    url(r'logout/$',logout,{'template_name':'core/logout.html'},name='logout'),
    #details_of_courses&proffesor
    url(r'^course/(?P<course_id>[0-9]+)$',views.detailc,name='detailc'),
    url(r'^prof/(?P<proffesor_id>[0-9]+)$',views.detailp,name='detailp'),
    #write review
    url(r'^course/(?P<course_id>[0-9]+)/re$',views.bleh,name='noice'),
    url(r'^prof/(?P<proffesor_id>[0-9]+)/re$',views.blep,name='noicep'),
    #helper_urls
    url(r'^course/(?P<course_id>[0-9]+)/r$',views.reviewc,name='reviewc'),
    url(r'^prof/(?P<proffesor_id>[0-9]+)/r$',views.reviewp,name='reviewp'),
]
