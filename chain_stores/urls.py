from django.urls import path

from chain_stores.views import SupplierCreateView

urlpatterns = [
    path('create/', SupplierCreateView.as_view(), name='create'),
    ]