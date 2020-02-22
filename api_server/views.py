from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from api_server.models import Point , TypeOfPoint
from api_server.serializers import PointSerializerDetail, TypeOfPointSerializer, PointSerializer
from api_server.permission import canCreatePoint
from django.db.models import Q

@api_view(['GET'])
def getByPos(request):
    try:
        x = request.GET.get('x')
        y = request.GET.get('y')

        # If no parameters are given, throw all models
        if x is None and y is None:
            return getAllPoints()
        points = Point.objects.get(latitude=x,longitude=y)
    except Point.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PointSerializer(points)
    return Response(serializer.data)

def getAllPoints():
        try:
            points = Point.objects.all()
        except Point.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PointSerializer(points, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getByID(request, pk):
    try:
        points = Point.objects.get(pk=pk)
    except Point.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PointSerializerDetail(points)
    return Response(serializer.data)

@api_view(['GET'])
def getByRange(request):
    try:
        x1 = request.GET['x1']
        x2 = request.GET['x2']
        y1 = request.GET['y1']
        y2 = request.GET['y2']

        points = Point.objects.filter((Q(latitude__lte=x1)&Q(latitude__gte=x2))&(Q(longitude__lte=y1)&Q(longitude__gte=y2)))
    except Point.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PointSerializer(points, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTypeByID(request, pk):
    try:
        types = TypeOfPoint.objects.get(pk=pk)
    except TypeOfPoint.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TypeOfPointSerializer(types)
    return Response(serializer.data)

# -----------POST------------

@api_view(['POST'])
@permission_classes([canCreatePoint])
def postPoint(request):

    serializer = PointSerializerDetail(data=request.data, context={'request': request})

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([canCreatePoint])
def postType(request):

    serializer = TypeOfPointSerializer(data=request.data, context={'request': request})

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
