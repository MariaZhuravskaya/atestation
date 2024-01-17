from rest_framework import serializers

from chain_stores.models import Supplier


class SupplierSerializers(serializers.ModelSerializer):
    """
    Сериализатор для представления привычки
    """
    class Meta:
        model = Supplier
        fields = '__all__'