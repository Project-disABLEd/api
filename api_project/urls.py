from django.urls import include, path
from rest_framework import routers
from api_server import views, urls as apiUrls

router = routers.DefaultRouter()
router.register(r'points', views.PointViewSet)
router.register(r'TypeOfPoint', views.TypeOfPointViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(apiUrls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
