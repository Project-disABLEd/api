from jose import jwt

from rest_framework.test import APITestCase
from rest_framework import status
from django.test import TestCase, Client
from django.db.models import Q

from api_server.models import Point , TypeOfPoint
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

        TypeOfPoint.objects.create(name="test")

        self.dataType = {
            'name': 'testType'
        }

        self.dataPoint = {'name': 'test',
             'source': 'test',
             'latitude': 1,
             'longitude': 1,
             'typeObj': 1
        }
        self.requreStatus = status.HTTP_201_CREATED
        self.token = Auth(self)

    def testPostType(self):
        url = '/api/points/types/add/'

        response = self.client.post(url, self.dataType, HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, self.requreStatus)


    def testPostPoint(self):
        url = '/api/points/add/'

        response = self.client.post(url, self.dataPoint, HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, self.requreStatus)
   

class GetTest(TestCase):

    def setUp(self):

        type = TypeOfPoint.objects.create(name="test")
        Point.objects.create(name="test", source='test', latitude=1, longitude=1, typeObj=type)

        self.requreStatus = status.HTTP_200_OK

    def testGetAllPoints(self):  
        url = '/api/points/'
        response = self.client.get(url)

        objects = Point.objects.all()
        serializer = PointSerializer(objects, many=True)

        self.assertEqual(response.status_code, self.requreStatus) 
        self.assertEqual(response.data, serializer.data)

    def testGetPointByPos(self): 
        url = '/api/points/pos/'
        x = 1
        y = 1

        response = self.client.get(url, {'x': x, 'y': y})
        
        objects = Point.objects.get(latitude=x,longitude=y)
        serializer = PointSerializer(objects)

        self.assertEqual(response.status_code, self.requreStatus) 
        self.assertEqual(response.data, serializer.data)
    
    def testGetPointByPhrase(self):
        url = '/api/points/search/'
        phrase = "t"

        response = self.client.get(url, {'phrase': phrase})

        objects = Point.objects.filter(Q(name__contains=phrase) or Q(desc__contains=phrase) or Q(site__contains=phrase) or Q(address__contains=phrase))
        serializer = PointSerializer(objects, many=True)

        self.assertEqual(response.status_code, self.requreStatus) 
        self.assertEqual(response.data, serializer.data)

    def testGetPointByRange(self):
        url = '/api/points/range/'
        x1 = 1
        x2 = -1
        y1 = 1
        y2 = -1

        response = self.client.get(url, {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2})

        objects = Point.objects.filter((Q(latitude__lte=x1) & Q(latitude__gte=x2)) & (Q(longitude__lte=y1) & Q(longitude__gte=y2)))
        serializer = PointSerializer(objects, many=True)

        self.assertEqual(response.status_code, self.requreStatus) 
        self.assertEqual(response.data, serializer.data)


    def testGetPointByID(self):
        id = 1
        url = '/api/points/'+str(id)+'/'

        response = self.client.get(url)

        objects = Point.objects.get(pk=id)
        serializer = PointSerializerDetail(objects)

        self.assertEqual(response.status_code, self.requreStatus) 
        self.assertEqual(response.data, serializer.data)


    def testGetPointByID(self):
        id = 1
        url = '/api/points/types/'+str(id)+'/'

        response = self.client.get(url)

        objects = TypeOfPoint.objects.get(pk=id)
        serializer = TypeOfPointSerializer(objects)

        self.assertEqual(response.status_code, self.requreStatus) 
        self.assertEqual(response.data, serializer.data)


class PatchTest(TestCase):

    def setUp(self):

        type = TypeOfPoint.objects.create(name="test")
        Point.objects.create(name="test", source='test', latitude=1, longitude=1, typeObj=type)

        self.dataType = {
            'name': 'test2'
        }

        self.dataPoint = {
            'name': 'test4',
            'latitude': 4
        }

        self.requreStatus = status.HTTP_202_ACCEPTED
        self.token = Auth(self)

    def testPatchType(self):
        id = 1
        url = '/api/points/types/edit/'+str(id)+'/'

        response = self.client.patch(url, self.dataType, content_type='application/json', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, self.requreStatus)


    def testPatchPoint(self):
        id = 1
        url = '/api/points/edit/'+str(id)+'/'

        response = self.client.patch(url, self.dataPoint, content_type='application/json', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, self.requreStatus)
   

class DeleteTest(TestCase):

    def setUp(self):

        type = TypeOfPoint.objects.create(name="test")
        Point.objects.create(name="test", source='test', latitude=1, longitude=1, typeObj=type)

        self.requreStatus = status.HTTP_204_NO_CONTENT
        self.token = Auth(self)

    def testDelType(self):
        id = 1
        url = '/api/points/types/del/'+str(id)+'/'

        response = self.client.delete(url, HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, self.requreStatus)


    def testDelPoint(self):
        id = 1
        url = '/api/points/del/'+str(id)+'/'

        response = self.client.delete(url, HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, self.requreStatus)