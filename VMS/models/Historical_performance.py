
from django.db import models
from .Vendor_details import Vendor 
from rest_framework import serializers

from .BaseModel import BaseModel
class HistoricalPerformance(BaseModel):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)



    def __str__(self):
        return str(self.vendor)
    

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = ('__all__')
        extra_kwargs = {
            'createdBy': {'required': False},
            'updatedBy': {'required': False},
            'vendor': {'required': False},
            'date': {'required': False},
            'on_time_delivery_rate': {'required': False},
            'quality_rating_avg': {'required': False},
            'average_response_time': {'required': False},
            'fulfillment_rate': {'required': False},
        }

    def to_representation(self, instance):     
        ret = super().to_representation(instance)
        if instance.average_response_time!=None:
            ret["average_response_time"]=str(ret['average_response_time'])+ "  hours"
        ret["vendor code"]=instance.vendor.vendor_code
        return ret