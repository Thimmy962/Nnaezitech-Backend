from django.contrib import admin
from .models import *


class ImageInline(admin.TabularInline):
    model = Car_Image
    extra = 1

class CarAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ["name", "price", "status"]
    search_fields = ["name", "price", "status"]
    list_filter = ["name", "price", "status"]

admin.site.register(Car, CarAdmin)

admin.site.register(Message)
admin.site.register(Company)