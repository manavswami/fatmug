from django.urls import path
# from VMS.views.Register import ResgisterView
from VMS.views.vendor_details import VendorDetailsView 
from VMS.views.Purchase_order import PurchaseDetailsView
from VMS.views.AcknowledgeView import AcknowledgeView
from VMS.views.Register import ResgisterView
from VMS.views.login import LoginView
from VMS.views.performance_matrix import PerformanceMatrixView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('vendors/', VendorDetailsView.as_view(), name='vendor_details'),
    path('vendors/<str:pk>/', VendorDetailsView.as_view(), name='vendor_details'),
    path('purchase_orders/', PurchaseDetailsView.as_view(), name='purchase_details'),
    path('purchase_orders/<str:pk>/', PurchaseDetailsView.as_view(), name='purchase_details'),
    path('purchase_orders/<str:pk>/acknowledge/', AcknowledgeView.as_view(), name='purchase_acknowledge'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registeruser/', ResgisterView.as_view(), name='register_user'),
    path('login/', LoginView.as_view(), name='token_login'),
    path('vendors/<str:pk>/performance/', PerformanceMatrixView.as_view(), name='vendor_performance'),

]