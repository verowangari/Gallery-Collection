import re
from django.urls import path
from . import views
urlpatterns=[
    # path('^$',views.welcome,name = 'welcome'),
    path('^today/$',views.photos_of_day,name='newsToday'),
    path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_photos,name = 'pastPhotos'),
    path('', views.gallery, name='gallery'),
    path('photo/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
    # <str:pk>/
    
]