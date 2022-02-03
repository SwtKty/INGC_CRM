from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', views.homeEmploye),

    path('employeAPI-list/', views.employeList),
    path('employeAPI-detail/<str:pk>/', views.employeDetail),
    path('addEmploye/', views.addEmploye),
    path('updateEmploye/<str:pk>/', views.UpdateEmploye),
    path('deleteEmploye/<str:pk>/', views.DeleteEmploye),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
