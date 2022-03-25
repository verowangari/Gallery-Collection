from django.conf.urls import path
from . import views
urlpatterns=[
    path('^$',views.welcome,name = 'welcome'),
]