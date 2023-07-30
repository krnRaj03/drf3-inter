from django.urls import path
from .views import *
#create urls here

urlpatterns = [
 path('watch-list/', MovieListAV.as_view(), name='watch-list'),
  path('watch-list/<int:pk>', MovieListDetailAV.as_view(), name='watch-list-detail'),

 path('stream-list/', StreamingPlatformAV.as_view(), name='stream-list'),
  path('stream-list/<int:pk>', StreamingPlatformListAV.as_view(), name='stream-list-detail'),
]
