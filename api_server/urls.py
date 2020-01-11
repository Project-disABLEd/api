from django.urls import include, path
from api_server.views import GetPoint

urlpatterns = [
    path('detail-point/', GetPoint.as_view()),
]