from jose import jwt
import os

SECRET_KEY_TOKEN_FILE = open("./api_project/secret_key_token.txt", "r")
SECRET_KEY_TOKEN = SECRET_KEY_TOKEN_FILE.read()
SECRET_KEY_TOKEN_FILE.close()


token = jwt.encode({'key': 'value'}, SECRET_KEY_TOKEN, algorithm='HS256')
print(token)
