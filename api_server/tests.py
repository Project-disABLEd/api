from django.urls import include, path, reverse
from rest_framework.test import APITestCase
from api_project import urls
from rest_framework import status


class AccountTests(APITestCase):

    def testPostPoints(self):
        url = '/api/points/types/add/'
        response = self.client.post(url, {'name': 'test'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)    

    def testPostPointsType(self):
        url = '/api/points/add/'
        response = self.client.post(url, {'name': 'test',
                                          'source': 'test',
                                          'latitude': 0,
                                          'longitude': 0,
                                          'typeObj': 1
                                          }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)    

    def testGetAllPoints(self):
        url = '/api/points/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

    def testGetPointsByPos(self):
        url = '/api/points/pos/'
        response = self.client.get(url, {'x': 1, 'y': 1}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

    def testGetPointsByRange(self):
        url = '/api/points/range/'
        response = self.client.get(url, {'x1': 1, 'y1': 1, 'x2': -1, 'y2': -1},format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK) 

    def testGetPointsByID(self):
        url = '/api/points/1/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        
    def testGetPointsTypeByID(self):
        url = '/api/points/types/1/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)    

    

