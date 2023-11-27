
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from VMS.models.Historical_performance import HistoricalPerformance,HistoricalPerformanceSerializer
from rest_framework.permissions import IsAuthenticated


class PerformanceMatrixView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request,pk=None):
        try:
            if pk:
                vendor_detail=HistoricalPerformance.objects.get(vendor__vendor_code=pk)
                serializer=HistoricalPerformanceSerializer(vendor_detail).data
            return Response({"data":serializer}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
        

