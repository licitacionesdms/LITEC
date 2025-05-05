# firebase_config.py
import pyrebase

firebase_config = {
    "apiKey": "AIzaSyB56k71mqe2ebmjABA4ckZd81vT8thUJew",
    "authDomain": "proyecto-a4977.firebaseapp.com",
    "projectId": "proyecto-a4977",
    "storageBucket": "proyecto-a4977.firebasestorage.app",
    "messagingSenderId": "785328408908",
    "appId": "1:785328408908:web:7412b8f6ba719f7b7a67e9",
    "databaseURL": "postgresql://admin:SwCTqxFKcGFOHRHpWsR1GW0h2Q3GIPBy@dpg-d0b9gs2dbo4c73ci1mj0-a.ohio-postgres.render.com/lh_db"
}

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
