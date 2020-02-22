from django.urls import include, path
from api_server import urls as apiUrls


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(apiUrls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
