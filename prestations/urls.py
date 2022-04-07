from django.urls import path
from . import views
from rest_framework.decorators import api_view


urlpatterns = [
    path('', views.home),
    path('prestations/', views.prestation),


    path('prestationAPI/', views.prestationOverview),
    path('prestationAPI-list/', views.prestationList),
    path('prestationAPI-detail/<str:pk>/', views.prestationDetail),
    path('addPrestation/', views.addPrestation),
    path('updatePrestation/<str:pk>/', views.UpdatePrestation),
    path('deletePrestation/<str:pk>/', views.DeletePrestation),

    path('prestation/', views.PrestationList.as_view()),
    path('prestation/<int:pk>', views.PrestationDetail.as_view())

]
