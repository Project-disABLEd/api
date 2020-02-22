from django.urls import path
from api_server.views import getByID, getByPos, getTypeByID, postPoint, postType

urlpatterns = [path('points/', getByPos),
    path('points/add/', postPoint),
    path('points/<int:pk>/', getByID),
    path('points/types/<int:pk>/', getTypeByID),
    path('points/types/add/', postType),]
