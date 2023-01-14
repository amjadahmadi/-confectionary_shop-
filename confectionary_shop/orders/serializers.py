from rest_framework import serializers
from .models import Orders, Order_Item


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Item
        fields = '__all__'

    def create(self, validated_data):
        stock = validated_data['stock_id']
        count = stock.count
        kilo = stock.kilo
        count_per_kilo = (kilo / count) if (count and kilo) else None

        if validated_data['kilo']:
            if kilo - validated_data['amount'] < 0:
                validated_data['order_status'] = 'CA'
            else:
                stock.kilo -= validated_data['amount']
                if count_per_kilo:
                    stock.count -= validated_data['amount'] / count_per_kilo

        else:
            if count - validated_data['amount'] < 0:
                validated_data['order_status'] = 'CA'
            else:
                stock.count -= validated_data['amount']
                if count_per_kilo:
                    stock.kilo -= validated_data['amount'] * count_per_kilo
        stock.save()
        return super(OrderItemSerializer, self).create(validated_data)
