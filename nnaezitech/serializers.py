from .models import *
from rest_framework import serializers

class CarSerializer(serializers.ModelSerializer):
    car_image = serializers.SerializerMethodField()
    make = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = "__all__"

    def get_car_image(self, obj):
        images = obj.images.all()
        if images:
            return [image.image.url for image in images]
        return None
    
    def get_make(self, obj):
        make = Company.objects.get(name = obj.make.name)
        return make.name



    



class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"





class CompanySerializer(serializers.ModelSerializer):
    cars = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = "__all__"

    
    def get_cars(self, obj):
        cars = obj.cars.all()
        return [CarSerializer(car).data for car in cars]