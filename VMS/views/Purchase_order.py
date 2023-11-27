
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from VMS.models.Purchase_order import PurchaseOrderDetails,PurchaseOrderDetailsSerializer
import uuid
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class PurchaseDetailsView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,pk=None):
        try:
            if pk:
                po = get_object_or_404(PurchaseOrderDetails, po_number=pk)
                serializer = PurchaseOrderDetailsSerializer(po)
            else:
                Vendorlist=PurchaseOrderDetails.objects.all()
                serializer = PurchaseOrderDetailsSerializer(Vendorlist,many=True).data
            return Response({"data":serializer}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
 
    def post(self, request):
        try:
            serializer = PurchaseOrderDetailsSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(po_number=uuid.uuid4().hex[:8])
                return Response({"data": "created sucessfully"}, status=status.HTTP_201_CREATED)
            return Response({"error":"bad request"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk,):
        if request.data.get("po_number"):
            del request.data["po_number"]
        try:
            instance =PurchaseOrderDetails.objects.get(po_number=pk)
        except PurchaseOrderDetails.DoesNotExist:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = PurchaseOrderDetailsSerializer(
            instance=instance, data=request.data, partial=True,)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"error":"unable to update the vandor details"},status=status.HTTP_400_BAD_REQUEST, )
        
    def delete(self, request, pk):
        try:
            instance =PurchaseOrderDetails.objects.get(vendor_code=pk)
        except PurchaseOrderDetails.DoesNotExist:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        if instance is not None:
            instance.delete()
            return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Vendor object not found"}, status=status.HTTP_404_NOT_FOUND)