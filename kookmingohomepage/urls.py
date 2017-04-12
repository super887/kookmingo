from django.conf.urls import url, include
from django.contrib import admin
from .views import *
from . import views


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^acocounts/register/done/$',UserCreateDoneTV.as_view(),name='register_done'),

    url(r'^crawl/', views.crawl),
    url(r'^delete/', views.delete),

    url(r'^hanul/$',HanulLV.as_view(),name='hanul'),
    url(r'^student/$', StudentLV.as_view(), name='student'),
    url(r'^staff/$', StaffLV.as_view(), name='staff'),
    url(r'^smell/$', SmellLV.as_view(), name='smell'),
    url(r'^dormitorynormal/$', DormitoryNormalLV.as_view(), name='dormitorynormal'),
    url(r'^dormitoryroutine/$', DormitoryRoutineLV.as_view(), name='dormitoryroutine'),

]
