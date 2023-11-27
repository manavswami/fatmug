
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from VMS.models.Historical_performance import HistoricalPerformance
from VMS.models.Purchase_order import PurchaseOrderDetails,PurchaseOrderDetailsSerializer
from django.db.models import Avg
from django.db import models
import datetime
from django.db.models import F, ExpressionWrapper, fields
from django.db.models.functions import Coalesce
from rest_framework.permissions import IsAuthenticated


class AcknowledgeView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request,pk=None):
        try:
            if pk:
                vendor_detail=PurchaseOrderDetails.objects.get(po_number=pk)
                vendor_detail.acknowledgment_date=datetime.datetime.now()
                
                #findg the avg time of response of vendor 
                avg_time_diff = PurchaseOrderDetails.objects.filter(vendor=vendor_detail.vendor).annotate(
                time_diff=ExpressionWrapper(
                    F('acknowledgment_date') - F('issue_date'),
                    output_field=fields.DurationField(),
                )
                ).aggregate(avg_time=Coalesce(Avg('time_diff'), 0))

                #storing response time in hours 
                total_hours = avg_time_diff['avg_time'].days * 24 + avg_time_diff['avg_time'].seconds / 3600 + avg_time_diff['avg_time'].microseconds / (3600 * 1e6)
                HistoricalPerformance_object,_=HistoricalPerformance.objects.get_or_create(vendor=vendor_detail.vendor)
                HistoricalPerformance_object.date=datetime.datetime.now()
                
                HistoricalPerformance_object.average_response_time=int(total_hours)
                HistoricalPerformance_object.save()
                vendor_detail.vendor.average_response_time=int(total_hours)
                vendor_detail.save()
            return Response({"data":"acknowledgment_date has been updated"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
        

