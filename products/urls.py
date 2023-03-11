from django.urls import path
from .views import populate_db

urlpatterns = [
    path('load_models/', populate_db, name='load'),
]
