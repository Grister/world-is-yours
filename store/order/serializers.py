from order.models import Order
from user.models import Address
from user.serializers import AddressSerializer
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        address_data = validated_data.pop('address', None)
        order_data = Order.objects.create(**validated_data)

        if address_data:
            address = Address.objects.create(**address_data)
            order_data.address = address
            order_data.save()

        return order_data
