from django.urls import include, path
from api_server.views import getByID,getByPos,getTypeByID,postPoint

urlpatterns = [
    path('points/', getByPos),
    path('points/add/', postPoint),
    path('points/<int:pk>/', getByID),
    path('type-of-point/<int:pk>/', getTypeByID),
]