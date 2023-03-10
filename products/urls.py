from django.urls import path
from .views import populate_models

urlpatterns = [
    path('load_models/', populate_models, name='load'),
]
