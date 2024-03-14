from django.urls import path
from weather_api.views import satellite_radar
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name="home"),
    path("result", views.result, name="result"),
     path('satellite_radar', views.satellite_radar, name="satellite_radar"),
    path('Alert', views.Alert, name="Alert"),
    path('Alert/<int:image_id>/', views.Alert, name='alert'),
 
     
    # path('social_links', views.social_links),
]


