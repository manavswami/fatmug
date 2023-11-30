from django.contrib import admin
from VMS.models.Vendor_details import Vendor
from VMS.models.Purchase_order import PurchaseOrderDetails

from VMS.models.Historical_performance import HistoricalPerformance

# Register your models here.
admin.site.register(Vendor)
admin.site.register(PurchaseOrderDetails)

admin.site.register(HistoricalPerformance)