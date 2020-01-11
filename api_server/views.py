from rest_framework import viewsets
from api_server.models import Point , TypeOfPoint
from api_server.serializers import PointSerializer , TypeOfPointSerializer


class PointViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Point.objects.all().order_by('-ID')
    serializer_class = PointSerializer

class TypeOfPointViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = TypeOfPoint.objects.all()
    serializer_class = TypeOfPointSerializer

    
from rest_framework.views import APIView
from rest_framework.response import Response

class GetPoint(APIView):
    def get(self, request):
        if request.method == 'GET':
            points = Point.objects.all()
            serializer = PointViewSet(points)
            return Response(serializer.data)
        else:
            return Response("no query")