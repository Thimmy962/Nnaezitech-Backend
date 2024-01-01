from django.db import models
import uuid

class Car_Image(models.Model):
    car = models.ForeignKey('Car', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/')


class Car(models.Model):
    STATUS_CHOICES = [
        ("Used", "USED"),
        ("New", "NEW")
    ]

    TRANSMISSION_CHOICES = [
        ("Manual", "Automatic"),
        ("Manual", "Manual")
    ]

    BODY_CHOICES = [
        ("Sedan", "Sedan"),
        ("SUV", "SUV"),
        ("Truck", "Truck"),
        ("Heavy Truck", "Heavy Truck")
    ]

    DRIVE_TRAIN = [
        ("All Wheel", "All Wheel"),
        ('Front Wheel', "Front Wheel"),
        ('Rear Wheel', 'Rear Wheel')
    ]

    CYLINDERS = [
            (4, 4),
            (6, 6),
            (8, 8),
            (12, 12)
        ]

    id = models.UUIDField(default=uuid.uuid4, editable=False, auto_created=True, unique=True, primary_key=True)
    name = models.CharField(max_length=256)
    price = models.IntegerField(default=1000)
    make = models.ForeignKey("Company", on_delete=models.CASCADE, related_name='cars', null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="used")
    model_year = models.CharField(max_length=4, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True)
    transmission = models.CharField(max_length=10, blank=True, null=True, choices=TRANSMISSION_CHOICES)
    body = models.CharField(max_length=15, blank=True, null=True, choices=BODY_CHOICES)
    drive_train = models.CharField(max_length=20, blank=True, null=True, choices=DRIVE_TRAIN)
    seats = models.IntegerField(blank=True, null=True)
    auxilliary = models.BooleanField(default=False)
    cylinders = models.IntegerField(blank=True, null=True, choices=CYLINDERS)
    

    def __str__(self):
        return self.name
    


    
    
class Company(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ("-id",)





class Message(models.Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=14)
    message = models.CharField(max_length=1024, default="Hello")
    mail = models.EmailField(default='oluwatimileyin962@gmail.com')
    timestamp = models.DateTimeField(auto_created=True, auto_now=True)
    attended = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
