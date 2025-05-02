import firebase_admin
from firebase_admin import credentials, auth

# Ruta del archivo JSON de Firebase (descárgalo desde Firebase Console)
FIREBASE_CREDENTIALS_PATH = "C:/Users/danna/djangotutorial/proyecto-a4977-firebase-adminsdk-fbsvc-10a1288fd4.json"

if not firebase_admin._apps:
    cred = credentials.Certificate(FIREBASE_CREDENTIALS_PATH)
    firebase_admin.initialize_app(cred)
