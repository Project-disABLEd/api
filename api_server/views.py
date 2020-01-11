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
        if request.method == 'POST':
            serializer = PointViewSet(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("no query")