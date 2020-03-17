from django.urls import path
from api_server.views import getByID, getByPos, getTypeByID, postPoint, postType, getByRange, getAll, search, editPoint, delPoint, editType, delType

urlpatterns = [
    path('points/', getAll),
    path('points/pos/', getByPos),
    path('points/range/', getByRange),
    path('points/add/', postPoint),
    path('points/search/', search),
    path('points/<int:pk>/', getByID),
    path('points/edit/<int:pk>/', editPoint),
    path('points/del/<int:pk>/', delPoint),
    path('points/types/<int:pk>/', getTypeByID),
    path('points/types/add/', postType),
    path('points/types/edit/<int:pk>/', editType),
    path('points/types/del/<int:pk>/', delType),
    ]
