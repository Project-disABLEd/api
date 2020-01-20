from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api_server.models import Point , TypeOfPoint
from api_server.serializers import PointSerializer , TypeOfPointSerializer

@api_view(['GET'])

def getByPos(request, format=None):

    if request.method == 'GET':
        try:
            x=request.GET.get('x')
            y=request.GET.get('y')

            # -------------if is no parameters trow all models------------------
            if x==None and y==None:
                try:
                    points = Point.objects.all()
                except Point.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                content={}
                for p in points:
                    content+={
                        'id': p.pk,
                        'name': p.name,
                        'latitude': p.latitude,
                        'longitude': p.longitude
                        }
                return Response(content)
            #-------------------------------------------------------------------

            points = Point.objects.get(latitude=x,longitude=y)

        except Point.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        content={
            'id': points.pk,
            'name': points.name,
            'latitude': points.latitude,
            'longitude': points.longitude
            }
        return Response(content)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])

def getByID(request, pk, format=None):
    if request.method == 'GET':
        try:
            points = Point.objects.get(pk=pk)
        except Point.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PointSerializer(points)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])

def getTypeByID(request, pk, format=None):
    if request.method == 'GET':
        try:
            type = TypeOfPoint.objects.get(pk=pk)
        except TypeOfPoint.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TypeOfPointSerializer(type)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)