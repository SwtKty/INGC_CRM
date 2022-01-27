from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('prestations/', views.prestation),


    path('prestationAPI/', views.prestationOverview),
    path('prestationAPI-list/', views.prestationList),
    path('prestationAPI-detail/<str:pk>/', views.prestationDetail),
    path('addPrestation/', views.addPrestation),
    path('updatePrestation/<str:pk>/', views.UpdatePrestation),
    path('deletePrestation/<str:pk>/', views.DeletePrestation)

]
