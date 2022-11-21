from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.Home),
    path('about', views.about),
    path('customer',views.customer),
]
