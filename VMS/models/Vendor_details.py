from django.db import models

# Create your models here.

from django.db import models

from rest_framework import serializers
from django.db import models

from .BaseModel import BaseModel


class Vendor(BaseModel):
    id = models.BigAutoField(primary_key = True)
    name = models.CharField(max_length=255,blank=True,null=True)
    contact_details=models.TextField()
    address=models.TextField()
    vendor_code = models.CharField(max_length=100,)
   


    def __str__(self):
        return self.vendor_code



class VendordetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('__all__')
        extra_kwargs = {
            'on_time_delivery_rate': {'required': False},
            'quality_rating_avg': {'required': False},
            'average_response_time': {'required': False},
            'fulfillment_rate': {'required': False},
            'vendor_code': {'required': False},
            'name': {'required': False},
        }
