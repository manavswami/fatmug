from django.db.models.signals import post_save
from django.dispatch import receiver
from VMS.models.Purchase_order import PurchaseOrderDetails
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

from VMS.models.Vendor_details import Vendor
from VMS.models.Historical_performance import HistoricalPerformance

@receiver(post_save, sender=PurchaseOrderDetails)
def handle_user_profile_save(sender, instance, created, **kwargs):
    try:
        HistoricalPerformance_object,_=HistoricalPerformance.objects.get_or_create(vendor=instance.vendor)
        
        total_completed_orders = PurchaseOrderDetails.objects.filter(vendor=instance.vendor, status='completed').count()
        if instance.status== "completed":
            # On-Time Delivery Rate
            on_time_delivery_count = PurchaseOrderDetails.objects.filter(
                vendor=instance.vendor, status='completed', actual_delivery__lte=models.F('delivery_date')
            ).count()
            instance.vendor.on_time_delivery_rate = (on_time_delivery_count / total_completed_orders) * 100 if total_completed_orders > 0 else 0
            HistoricalPerformance_object.on_time_delivery_rate=instance.vendor.on_time_delivery_rate
            # Quality Rating Average
            completed_orders_with_rating = PurchaseOrderDetails.objects.filter(vendor=instance.vendor, status='completed', quality_rating__isnull=False)
            total_ratings = completed_orders_with_rating.aggregate(models.Avg('quality_rating'))['quality_rating__avg']
            instance.vendor.quality_rating_avg = total_ratings if total_ratings else 0
            HistoricalPerformance_object.quality_rating_avg=instance.vendor.quality_rating_avg 
        total_orders = PurchaseOrderDetails.objects.filter(vendor=instance.vendor,).count()
        
        # Fulfilment Rate
        fulfillment_rate = (total_completed_orders / total_orders) * 100 if total_orders > 0 else 0
        instance.vendor.fulfillment_rate=fulfillment_rate
        instance.vendor.save()
        HistoricalPerformance_object.fulfillment_rate=fulfillment_rate
        HistoricalPerformance_object.save()
    except:
        pass


@receiver(post_save, sender=Vendor)
def Vendor_user_profile_save(sender, instance, created, **kwargs):
    try:
        obj, created =HistoricalPerformance.objects.get_or_create(vendor=instance)
    except:
        pass

