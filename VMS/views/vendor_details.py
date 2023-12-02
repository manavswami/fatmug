
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.response import Response
from VMS.models.Vendor_details import Vendor,VendordetailsSerializer
import uuid
from rest_framework.permissions import IsAuthenticated


class VendorDetailsView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request,pk=None):
        try:
            if pk:
                vendor_detail=Vendor.objects.get(vendor_code=pk)
                serializer = VendordetailsSerializer(vendor_detail).data
            else:
                Vendorlist=Vendor.objects.all()
                serializer = VendordetailsSerializer(Vendorlist,many=True).data
            return Response({"data":serializer}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
 
    def post(self, request):
        try:
            name=request.data.get("name")
            if name: 
                name=" ".join(name.split())
                request.data['name']=name
            contact_details=request.data.get("contact_details")
            if contact_details:
                contact_details=" ".join(contact_details.split()) #removing all extra space from text
                request.data['contact_details']=contact_details
            address=request.data.get("address")
            if address:
                address=" ".join(address.split()) #removing all extra space from text
                request.data['address']=address
            if contact_details ==None  or address== None or name==None:
                return Response({"Error": f"for creating Vendor 'contact_details', 'name' , and 'address'  fields are required"}, status=status.HTTP_400_BAD_REQUEST)
            object_exit_or_not=Vendor.objects.filter(contact_details=contact_details,  address=address,name=name ).exists()
            if object_exit_or_not:
                return Response({"Error": f"Vendor already exits with given contact_details '{contact_details} ' address '{address}'  and name '{name}' "}, status=status.HTTP_400_BAD_REQUEST)
            vendor_code_uuid=uuid.uuid4().hex[:8]
            
            serializer = VendordetailsSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(  vendor_code=vendor_code_uuid, 
                )
            return Response({"data":serializer.data}, status=status.HTTP_201_CREATED,content_type="application/json")        
        except Exception :  
            return Response({"Error": "error while creating vendor object"}, status=status.HTTP_400_BAD_REQUEST,content_type="application/json")
    def put(self, request, pk,):
        
        try:
            instance =Vendor.objects.get(vendor_code=pk)
        except Vendor.DoesNotExist:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        updated_data={}
        name=request.data.get("name")
        if name: 
            name=" ".join(name.split())
            updated_data.update({'name':name})
        contact_details=request.data.get("contact_details")
        if contact_details:
                contact_details=" ".join(contact_details.split())
                updated_data.update({'contact_details':contact_details})
        address=request.data.get("address")
        if address:
            address=" ".join(address.split())
            updated_data.update({'address':address})
        object_exit_or_not=Vendor.objects.filter(contact_details=contact_details,  address=address,name=name ).exclude(vendor_code=pk).exists()
        if object_exit_or_not:
                return Response({"Error": f"Vendor already exits with given contact_details '{contact_details}' address '{address}' name  '{name}' "}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = VendordetailsSerializer(
            instance=instance, data=updated_data, partial=True,)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response({"error":"unable to update the vandor details"},status=status.HTTP_400_BAD_REQUEST, )
        
    def delete(self, request, pk):
        try:
            instance =Vendor.objects.get(vendor_code=pk)
        except Vendor.DoesNotExist:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        if instance is not None:
            instance.delete()
            return Response({"message": "Object deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "Vendor object not found"}, status=status.HTTP_404_NOT_FOUND)