from django.urls import path
from . import views


urlpatterns = [
    path('', views.homeEmploye),
    path('employeAPI-list/', views.employeList),
    path('employeAPI-detail/<str:pk>/', views.employeDetail),
    path('addEmploye/', views.addEmploye),
    path('updateEmploye/<str:pk>/', views.UpdateEmploye),
    path('deleteEmploye/<str:pk>/', views.DeleteEmploye)
]
