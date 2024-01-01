from django.shortcuts import render
from rest_framework import generics, response, status
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from django.db.models import Q

class GetCars(generics.ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        query = self.request.GET.get("query", "")
        if query.title() == 'Old':
            query = 'used'
        try:
            price = int(query)
        except:
            price = 0
        return Car.objects.filter(Q(name__icontains=query) | Q(make__name__icontains=query) | 
                                  Q(color__icontains = query) | Q(status__icontains = query) | Q(price__lte = price)
                                  ).order_by('-id')


getcars = GetCars.as_view()



class GetCar(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

getcar = GetCar.as_view()



class Save_Message(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            return super().perform_create(serializer)

save_message = Save_Message.as_view()


class Companies(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


companies = Companies.as_view()


class Company(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

company = Company.as_view()


class CarBasedOnStatus(generics.ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        status = self.kwargs["status"]
        return Car.objects.filter(status = status.title())

CarBasedOnStatus = CarBasedOnStatus.as_view()