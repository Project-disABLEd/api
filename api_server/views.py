from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from api_server.models import Point , TypeOfPoint
from api_server.serializers import PointSerializerDetail, TypeOfPointSerializer, PointSerializer
from api_server.permission import canCreatePoint
from django.db.models import Q
from django.utils.datastructures import MultiValueDictKeyError

@api_view(['GET'])
def getByPos(request):
    try:
        x = request.GET['x']
        y = request.GET['y']

        points = Point.objects.get(latitude=x,longitude=y)
    except Point.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except MultiValueDictKeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer = PointSerializer(points)
    return Response(serializer.data)

@api_view(['GET'])
def getAll(request):
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
def search(request):
    try:
        s = request.GET['phrase']

        points = Point.objects.filter(Q(name__contains=s) or Q(desc__contains=s) or Q(site__contains=s) or Q(address__contains=s))
    except Point.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except MultiValueDictKeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer = PointSerializer(points, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getByRange(request):
    try:
        x1 = request.GET['x1']
        x2 = request.GET['x2']
        y1 = request.GET['y1']
        y2 = request.GET['y2']

        points = Point.objects.filter((Q(latitude__lte=x1) & Q(latitude__gte=x2)) & (Q(longitude__lte=y1) & Q(longitude__gte=y2)))
    except Point.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except MultiValueDictKeyError:
        return Response(status=status.HTTP_400_BAD_REQUEST)

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
