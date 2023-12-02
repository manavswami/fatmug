from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Vendor
from .models.Purchase_order import PurchaseOrderDetails,PurchaseOrderDetailsSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.serializers import serialize

class VendorModelTests(APITestCase):
    def setUp(self):
        self.vendor1 = Vendor.objects.create(
            name="Test1 Vendor",
            contact_details="111-111-111",
            address="Test1 Address",
            vendor_code="TEST001"
        )
        self.vendor2 = Vendor.objects.create(
            name="Test2 Vendor",
            contact_details="222-222-222",
            address="Test2 Address",
            vendor_code="TEST002"
        )
        self.url = reverse('vendor_details') 

        self.user = User.objects.create_user(username='testuser', password='testpassword')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

    def test_get_item_list(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["data"]), 2)

    def test_get_item_detail(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.get(reverse('vendor_details', args=[self.vendor2.vendor_code]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"]['name'], "Test2 Vendor")

    def test_create_item_sucess(self):
        data = {
                'name' : "Test3 Vendor",
                'contact_details' : "333-333-333",
                'address' : "Test1 Address",
                'vendor_code' : "TEST001"
                }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(), 3)

    def test_create_item_fail(self):
        data = {
                'name' : "Test3 Vendor",
                }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Vendor.objects.count(), 2)

    def test_update_item_sucess(self):
        data = {'name': 'Updated name', 'address': 'Updated address'}
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.put(reverse('vendor_details', args=[self.vendor2.vendor_code]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Vendor.objects.get(vendor_code=self.vendor2.vendor_code).name, 'Updated name')

    def test_update_item_fail(self):
        data = {'name': 'Updated name', 'address': 'Updated address'}
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.put(reverse('vendor_details', args=[999]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_vendor(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.delete(reverse('vendor_details', args=[self.vendor1.vendor_code]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Vendor.objects.filter(pk=self.vendor1.pk).exists())

    def test_delete_nonexistent_item(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.delete(reverse('vendor_details', args=[999]))  # Nonexistent item ID
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_item_vendor_performance_detail(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post(reverse('vendor_performance', args=[self.vendor2.vendor_code]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"]['vendor code'], "TEST002")




class POModelTests(APITestCase):
    def setUp(self):
        self.vendor1 = Vendor.objects.create(
            name="Test1 Vendor",
            contact_details="111-111-111",
            address="Test1 Address",
            vendor_code="TEST001"
        )
        self.vendor2 = Vendor.objects.create(
            name="Test2 Vendor",
            contact_details="222-222-222",
            address="Test2 Address",
            vendor_code="TEST002"
        )
        self.PO1= PurchaseOrderDetails.objects.create(
        po_number=111,
        issue_date="2023-11-25T12:47:36.031324Z",
        order_date= "2023-11-25",
        delivery_date= "2023-11-26",
        actual_delivery="2023-11-27",
        items= 1,
        quantity= 1,
        status= "pending",
        quality_rating= 1.0,
        acknowledgment_date= None,
        vendor= self.vendor1
        )
        self.PO2 = PurchaseOrderDetails.objects.create(
            po_number=222,
            issue_date="2023-11-25T12:47:36.031324Z",
            order_date= "2023-11-25",
            delivery_date= "2023-11-26",
            actual_delivery="2023-11-27",
            items= 2,
            quantity= 2,
            status= "pending",
            quality_rating= 2.0,
            acknowledgment_date= None,
            vendor= self.vendor2
        )

        self.url = reverse('purchase_details') 

        self.user = User.objects.create_user(username='testuser', password='testpassword')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

    def test_get_item_list(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["data"]), 2)

    def test_get_item_detail(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.get(reverse('purchase_details', args=[self.PO2.po_number]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"]['items'], 2)

    def test_create_item_sucess(self):
        data = {
            "po_number":333,
            "issue_date":"2023-11-25T12:47:36.031324Z",
            "order_date": "2023-11-25",
            "delivery_date": "2023-11-26",
            "actual_delivery":"2023-11-27",
            "items": 33,
            "quantity": 33,
            "status": "pending",
            "quality_rating": 33.0,
            "acknowledgment_date": None,
            "vendor": self.vendor2.id,
                }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        serializer = PurchaseOrderDetailsSerializer(data=data)
        if not serializer.is_valid():
            print(serializer.errors)
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrderDetails.objects.count(), 3)

    def test_create_item_fail(self):
        data = {
            "order_date": "2023-11-25",
            "delivery_date": "2023-11-26",
            "actual_delivery":"2023-11-27",
            "items": 33,
            "quantity": 33,
            "status": "pending",
            "quality_rating": 33.0,
            "acknowledgment_date": None,
            "vendor": self.vendor2.id,
                }

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(PurchaseOrderDetails.objects.count(), 2)


    def test_update_item_sucess(self):
        data = {
            "quantity": 44,
            "status": "completed",
            }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.put(reverse('purchase_details', args=[self.PO2.po_number]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(PurchaseOrderDetails.objects.get(po_number=self.PO2.po_number).status, 'completed')

    def test_update_item_fail(self):
        data = {
            "quantity": 44,
            "status": "completed",
            
            }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.put(reverse('purchase_details', args=[999]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_po(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}') 
        response = self.client.delete(reverse('purchase_details', args=[self.PO2.po_number]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(PurchaseOrderDetails.objects.filter(po_number=self.PO2.po_number).exists())

    def test_delete_nonexistent_item(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.delete(reverse('purchase_details', args=[999]))  # Nonexistent item ID
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_acknowledge_fail(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}') 
        response = self.client.post(reverse('purchase_acknowledge', args=[999]))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_acknowledge_sucess(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}') 
        response = self.client.post(reverse('purchase_acknowledge', args=[self.PO2.po_number]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
