
from rest_framework import serializers
from django.db import models


from .Vendor_details import Vendor


status_choices = (
    ('pending', 'pending'),
    ('completed', 'completed'),
    ('canceled', 'canceled'),

)


class PurchaseOrderDetails(models.Model):
    id = models.BigAutoField(primary_key = True)
    po_number=models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=False)
    order_date=models.DateTimeField(auto_now_add=True)
    delivery_date=models.DateField() #expected dilivery date
    items=models.JSONField()
    quantity = models.IntegerField()
    status= models.CharField(choices= status_choices, max_length=100)
    actual_delivery=models.DateField() #actual delivery that when product reach to customer
    quality_rating=models.FloatField(null=True, blank=True)
    issue_date=models.DateTimeField()
    acknowledgment_date=models.DateTimeField( null=True, blank=True)

    def __str__(self):
        return self.po_number
    


class PurchaseOrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderDetails
        fields = ('__all__')
        extra_kwargs = {
            'po_number': {'required': False},
            'vendor': {'required': False},
            'order_date': {'required': False},
            'delivery_date': {'required': False},
            'items': {'required': False},
            'quantity': {'required': False},
            'status': {'required': False},
            'quality_rating': {'required': False},
            'acknowledgment_date': {'required': False},
            
        }
    def to_representation(self, instance):     
        ret = super().to_representation(instance)
        ret["vendor_id"]=instance.vendor.id
        ret["vendor_code"]=instance.vendor.vendor_code
        del ret["vendor"]
        return ret



