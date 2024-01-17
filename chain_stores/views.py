from django.shortcuts import render
from rest_framework import generics

from chain_stores.models import Supplier, SupplierType
from chain_stores.serializers import SupplierSerializers


class SupplierCreateView(generics.CreateAPIView):
    """
    Представление для создания привычки
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializers

    def post(self, request, *args, **kwargs):
        if self.type == SupplierType.ZAVOD.value:
            self.level = 0
        else:
            if self.parent is not None:
                parent = Supplier.objects.get(pk=self.parent.pk)
                if parent.type == SupplierType.ZAVOD.value and self.type == SupplierType.RC.value:
                    self.level = 1
        return self.create(request, *args, **kwargs)



