import firebase_admin
from firebase_admin import credentials
from django.conf import settings

cred = credentials.Certificate(settings.BASE_DIR / "firebase-adminsdk.json")
firebase_admin.initialize_app(cred)
