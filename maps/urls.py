from django.urls import path                                                                                                                            
from maps import views

urlpatterns = [ 
    path('', views.map, name="map"),
]