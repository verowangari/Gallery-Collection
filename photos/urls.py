import re
from django.urls import re_path
from . import views
urlpatterns=[
    re_path('^$',views.welcome,name = 'welcome'),
    re_path('^today/$',views.photos_of_day,name='newsToday'),
    re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_photos,name = 'pastPhotos'),
    re_path('',views.gallery,name='gallery'),
    re_path('photo/str:pk',views.viewPhoto,name='photo'),
    re_path('add/',views.addPhoto,name='add'),
    
    
]