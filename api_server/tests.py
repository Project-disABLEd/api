from rest_framework.test import APITestCase
from rest_framework import status
from jose import jwt

class AccountTests(APITestCase):

    def testOneBigTest(self):

        #-------Authorization-------
        print("A")
        SECRET_KEY_TOKEN_FILE = open("./api_project/secret_key_token.txt", "r")
        SECRET_KEY_TOKEN = SECRET_KEY_TOKEN_FILE.read()
        SECRET_KEY_TOKEN_FILE.close()
        token = jwt.encode({'key': 'value'}, SECRET_KEY_TOKEN, algorithm='HS256')
        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        #-------Test Post-------
        url = '/api/points/types/add/'
        requreStatus = status.HTTP_201_CREATED
        response = self.client.post(url, {'name': 'test'}, format='json')
        
        self.assertEqual(response.status_code, requreStatus)
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
        self.assertEqual(response.status_code, requreStatus)    
        if(response.status_code == requreStatus):
            print("P")
        else:
            print("Error")
   
        #-------Test Get-------
        url = '/api/points/'
        requreStatus = status.HTTP_200_OK
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, requreStatus) 
        if(response.status_code == requreStatus):
            print("G")
        else:
            print("Error")

        #-------Test Get-------
        url = '/api/points/pos/'
        requreStatus = status.HTTP_200_OK
        response = self.client.get(url, {'x': 1, 'y': 1}, format='json')
        self.assertEqual(response.status_code, requreStatus) 
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

        #-------Test Patch-------
        url = '/api/points/types/edit/1/'
        requreStatus = status.HTTP_202_ACCEPTED
        response = self.client.patch(url, {'name': 'test2'}, format='json')
        self.assertEqual(response.status_code, requreStatus)    
        if(response.status_code == requreStatus):
            print("H")
        else:
            print("Error")

        #-------Test Patch-------
        url = '/api/points/edit/1/'
        requreStatus = status.HTTP_202_ACCEPTED
        response = self.client.patch(url, {'name': 'test2', 'latitude': 4}, format='json')
        self.assertEqual(response.status_code, requreStatus)    
        if(response.status_code == requreStatus):
            print("H")
        else:
            print("Error")

        #-------Test Delete-------
        url = '/api/points/del/1/'
        requreStatus = status.HTTP_204_NO_CONTENT
        response = self.client.delete(url)
        self.assertEqual(response.status_code, requreStatus)    
        if(response.status_code == requreStatus):
            print("D")
        else:
            print("Error")

         #-------Test Delete-------
        url = '/api/points/types/del/1/'
        requreStatus = status.HTTP_204_NO_CONTENT
        response = self.client.delete(url)
        self.assertEqual(response.status_code, requreStatus)    
        if(response.status_code == requreStatus):
            print("D")
        else:
            print("Error")
