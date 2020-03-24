from jose import jwt

from rest_framework import status
from django.test import TestCase
from django.db.models import Q

from api_server.models import Point, TypeOfPoint
from api_server.serializers import PointSerializerDetail, TypeOfPointSerializer, PointSerializer

#-------Authorization-------
def Auth(self):
    SECRET_KEY_TOKEN_FILE = open("./api_project/secret_key_token.txt", "r")
    SECRET_KEY_TOKEN = SECRET_KEY_TOKEN_FILE.read()
    SECRET_KEY_TOKEN_FILE.close()
    token = jwt.encode({'key': 'value'}, SECRET_KEY_TOKEN, algorithm='HS256')

    return 'Bearer ' + token

class PostTest(TestCase):
    def setUp(self):
        TypeOfPoint.objects.create(name="test") # Create a type for point creation

        self.dataType = {
            'name': 'testType'
        }

        self.dataPoint = {
            'name': 'test',
            'source': 'test',
            'latitude': 1,
            'longitude': 1,
            'typeObj': 1
        }
        self.requiredStatus = status.HTTP_201_CREATED
        self.token = Auth(self)

    def testPostType(self):
        url = '/api/points/types/add/'
        response = self.client.post(url, self.dataType, HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, self.requiredStatus)
        self.assertEqual(TypeOfPoint.objects.count(), 2) # Setting it to 2 is necessary due to test DB reset before tests. (Initial type is required for the point creation)

    def testPostPoint(self):
        url = '/api/points/add/'
        response = self.client.post(url, self.dataPoint, HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, self.requiredStatus)
        self.assertEqual(Point.objects.count(), 1)

    def testPostTypeNoToken(self):
        self.requiredStatus = status.HTTP_403_FORBIDDEN

        url = '/api/points/types/add/'
        response = self.client.post(url, self.dataType)

        self.assertEqual(response.status_code, self.requiredStatus)
        self.assertEqual(TypeOfPoint.objects.count(), 1)

    def testPostPointNoToken(self):
        self.requiredStatus = status.HTTP_403_FORBIDDEN

        url = '/api/points/add/'
        response = self.client.post(url, self.dataPoint)

        self.assertEqual(response.status_code, self.requiredStatus)
        self.assertEqual(Point.objects.count(), 0)

    def testPostTypeWrongToken(self):
        self.requiredStatus = status.HTTP_403_FORBIDDEN
        self.token = 'test'

        url = '/api/points/types/add/'
        response = self.client.post(url, self.dataType, HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, self.requiredStatus)
        self.assertEqual(TypeOfPoint.objects.count(), 1)

    def testPostPointWrongToken(self):
        self.requiredStatus = status.HTTP_403_FORBIDDEN
        self.token = 'test'

        url = '/api/points/add/'
        response = self.client.post(url, self.dataPoint, HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, self.requiredStatus)
        self.assertEqual(Point.objects.count(), 0)

class GetTest(TestCase):
    def setUp(self):
        self.TypeId = 1
        self.PointId = 1
        self.x = 1
        self.y = 1
        self.phrase = "t"

        self.type = TypeOfPoint.objects.create(name="test")
        Point.objects.create(name="test", source='test', latitude=self.x, longitude=self.y, typeObj=self.type)

        self.requiredStatus = status.HTTP_200_OK

    def testGetAllPoints(self):
        url = '/api/points/'
        response = self.client.get(url)

        objects = Point.objects.all()
        serializer = PointSerializer(objects, many=True)

        self.assertEqual(response.status_code, self.requiredStatus)
        self.assertEqual(response.data, serializer.data)

    def testGetPointByPos(self):
        url = '/api/points/pos/'
        response = self.client.get(url, {'x': self.x, 'y': self.y})

        objects = Point.objects.get(latitude=self.x,longitude=self.y)
        serializer = PointSerializer(objects)

        self.assertEqual(response.status_code, self.requiredStatus)
        self.assertEqual(response.data, serializer.data)

    def testGetPointByPhrase(self):
        url = '/api/points/search/'
        response = self.client.get(url, {'phrase': self.phrase})

        objects = Point.objects.filter(Q(name__contains=self.phrase) or Q(desc__contains=self.phrase) or Q(site__contains=self.phrase) or Q(address__contains=self.phrase))
        serializer = PointSerializer(objects, many=True)

        self.assertEqual(response.status_code, self.requiredStatus)
        self.assertEqual(response.data, serializer.data)

    def testGetPointByRange(self):
        url = '/api/points/range/'
        response = self.client.get(url, {'x1': self.x+1, 'y1': self.y+1, 'x2': self.x-1, 'y2': self.y-1})

        objects = Point.objects.filter((Q(latitude__lte=self.x+1) & Q(latitude__gte=self.x-1)) & (Q(longitude__lte=self.y+1) & Q(longitude__gte=self.y-1)))
        serializer = PointSerializer(objects, many=True)

        self.assertEqual(response.status_code, self.requiredStatus)
        self.assertEqual(response.data, serializer.data)

    def testGetPointByID(self):
        url = '/api/points/'+str(self.PointId)+'/'
        response = self.client.get(url)

        objects = Point.objects.get(pk=self.PointId)
        serializer = PointSerializerDetail(objects)

        self.assertEqual(response.status_code, self.requiredStatus)
        self.assertEqual(response.data, serializer.data)

    def testGetTypeByID(self):
        url = '/api/points/types/'+str(self.TypeId)+'/'
        response = self.client.get(url)

        objects = TypeOfPoint.objects.get(pk=self.TypeId)
        serializer = TypeOfPointSerializer(objects)

        self.assertEqual(response.status_code, self.requiredStatus)
        self.assertEqual(response.data, serializer.data)

class PatchTest(TestCase):
    def setUp(self):
        self.TypeId = 1
        self.PointId = 1
        self.type = TypeOfPoint.objects.create(name="test")
        Point.objects.create(name="test", source='test', latitude=1, longitude=1, typeObj=self.type)

        self.dataType = {
            'name': 'test2'
        }

        self.dataPoint = {
            'name': 'test4',
            'latitude': 4
        }

        self.requiredStatus = status.HTTP_202_ACCEPTED
        self.token = Auth(self)

    def testPatchType(self):
        url = '/api/points/types/edit/'+str(self.TypeId)+'/'
        response = self.client.patch(url, self.dataType, content_type='application/json', HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, self.requiredStatus)

    def testPatchPoint(self):
        url = '/api/points/edit/'+str(self.PointId)+'/'
        response = self.client.patch(url, self.dataPoint, content_type='application/json', HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, self.requiredStatus)

    def testPatchTypeNoToken(self):
        self.requiredStatus = status.HTTP_403_FORBIDDEN
        url = '/api/points/types/edit/'+str(self.TypeId)+'/'
        response = self.client.patch(url, self.dataType, content_type='application/json')

        self.assertEqual(response.status_code, self.requiredStatus)

    def testPatchPointNoToken(self):
        self.requiredStatus = status.HTTP_403_FORBIDDEN
        url = '/api/points/edit/'+str(self.PointId)+'/'
        response = self.client.patch(url, self.dataPoint, content_type='application/json')

        self.assertEqual(response.status_code, self.requiredStatus)

    def testPatchTypeWrongToken(self):
        self.requiredStatus = status.HTTP_403_FORBIDDEN
        self.token = 'test'

        url = '/api/points/types/edit/'+str(self.TypeId)+'/'
        response = self.client.patch(url, self.dataType, content_type='application/json', HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, self.requiredStatus)

    def testPatchPointWrongToken(self):
        self.requiredStatus = status.HTTP_403_FORBIDDEN
        self.token = 'test'

        url = '/api/points/edit/'+str(self.PointId)+'/'
        response = self.client.patch(url, self.dataPoint, content_type='application/json', HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, self.requiredStatus)

class DeleteTest(TestCase):
    def setUp(self):
        self.TypeId = 1
        self.PointId = 1

        self.type = TypeOfPoint.objects.create(name="test")
        Point.objects.create(name="test", source='test', latitude=1, longitude=1, typeObj=self.type)

        self.requiredStatus = status.HTTP_204_NO_CONTENT
        self.token = Auth(self)

    def testDelType(self):
        url = '/api/points/types/del/'+str(self.TypeId)+'/'
        response = self.client.delete(url, HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, self.requiredStatus)
        self.assertEqual(TypeOfPoint.objects.count(), 0)

    def testDelPoint(self):
        url = '/api/points/del/'+str(self.PointId)+'/'
        response = self.client.delete(url, HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, self.requiredStatus)
        self.assertEqual(Point.objects.count(), 0)

    def testDelTypeNoToken(self):
        self.requiredStatus = status.HTTP_403_FORBIDDEN
        url = '/api/points/types/del/'+str(self.TypeId)+'/'
        response = self.client.delete(url)

        self.assertEqual(response.status_code, self.requiredStatus)
        self.assertEqual(TypeOfPoint.objects.count(), 1)

    def testDelPointNoToken(self):
        self.requiredStatus = status.HTTP_403_FORBIDDEN
        url = '/api/points/del/'+str(self.PointId)+'/'
        response = self.client.delete(url)

        self.assertEqual(response.status_code, self.requiredStatus)
        self.assertEqual(Point.objects.count(), 1)

    def testDelTypeWrongToken(self):
        self.requiredStatus = status.HTTP_403_FORBIDDEN
        self.token = 'test'

        url = '/api/points/types/del/'+str(self.TypeId)+'/'
        response = self.client.delete(url, HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, self.requiredStatus)
        self.assertEqual(TypeOfPoint.objects.count(), 1)

    def testDelPointWrongToken(self):
        self.requiredStatus = status.HTTP_403_FORBIDDEN
        self.token = 'test'

        url = '/api/points/del/'+str(self.PointId)+'/'
        response = self.client.delete(url, HTTP_AUTHORIZATION=self.token)

        self.assertEqual(response.status_code, self.requiredStatus)
        self.assertEqual(Point.objects.count(), 1)
