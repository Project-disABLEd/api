from rest_framework.test import APITestCase
from rest_framework import status


class AccountTests(APITestCase):

    def testOneBigTest(self):

        #-------Test Post-------
        url = '/api/points/types/add/'
        requreStatus = status.HTTP_201_CREATED
        response = self.client.post(url, {'pk': 1, 'name': 'test'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        if(response.status_code == requreStatus):
            print("P")
        else:
            print("Error")

        #-------Test Post-------
        url = '/api/points/add/'
        requreStatus = status.HTTP_201_CREATED
        response = self.client.post(url, {'name': 'test',
                                          'source': 'test',
                                          'latitude': 1,
                                          'longitude': 1,
                                          'typeObj': 1
                                          }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)    
        if(response.status_code == requreStatus):
            print("P")
        else:
            print("Error")
   
        #-------Test Get-------
        url = '/api/points/'
        requreStatus = status.HTTP_200_OK
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        if(response.status_code == requreStatus):
            print("G")
        else:
            print("Error")

        #-------Test Get-------
        url = '/api/points/pos/'
        requreStatus = status.HTTP_200_OK
        response = self.client.get(url, {'x': 1, 'y': 1}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        if(response.status_code == requreStatus):
            print("G")
        else:
            print("Error")
    
        #-------Test Get-------
        url = '/api/points/search/'
        requreStatus = status.HTTP_200_OK
        response = self.client.get(url, {'phrase': "test"},format='json')
        self.assertEqual(response.status_code, requreStatus)
        if(response.status_code == requreStatus):
            print("G")
        else:
            print("Error")

        #-------Test Get-------
        url = '/api/points/range/'
        requreStatus = status.HTTP_200_OK
        response = self.client.get(url, {'x1': 1, 'y1': 1, 'x2': -1, 'y2': -1},format='json')
        self.assertEqual(response.status_code, requreStatus)
        if(response.status_code == requreStatus):
            print("G")
        else:
            print("Error")

        #-------Test Get-------
        url = '/api/points/1/'
        requreStatus = status.HTTP_200_OK
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, requreStatus) 
        if(response.status_code == requreStatus):
            print("G")
        else:
            print("Error")

        #-------Test Get-------
        url = '/api/points/types/1/'
        requreStatus = status.HTTP_200_OK
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, requreStatus)    
        if(response.status_code == requreStatus):
            print("G")
        else:
            print("Error")
