from django.urls import path
from .views import *

urlpatterns = [
    path("getcars/", getcars),
    path("getcars/<str:status>/", CarBasedOnStatus),
    path("getcar/<str:pk>/", getcar),
    path("new_message", save_message),
    path('companies/', companies),
    path('company/<int:pk>/', company)
]